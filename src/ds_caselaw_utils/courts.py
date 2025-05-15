# mypy: disable-error-code="override"

"""
Get metadata for the courts covered by the service
"""

import pathlib
from datetime import date
from enum import Enum
from functools import cached_property
from re import compile
from typing import Any, Dict, Optional

from markdown_it import MarkdownIt
from mdit_py_plugins.attrs import attrs_plugin
from ruamel.yaml import YAML

from ds_caselaw_utils.types.courts_schema_autogen import (
    RawCourt,
    RawCourtRepository,
    RawJurisdiction,
)

from .types import CourtCode, CourtParam, JurisdictionCode, NeutralCitationPattern

md = MarkdownIt("commonmark", {"breaks": True, "html": True}).use(attrs_plugin)


class InstitutionType(Enum):
    COURT = "court"
    TRIBUNAL = "tribunal"


class Jurisdiction:
    def __init__(self, data: RawJurisdiction):
        self.code: JurisdictionCode = JurisdictionCode(data["code"])
        self.name: str = data["name"]
        self.prefix: Optional[str] = data.get("prefix")


class Court:
    def __init__(self, data: RawCourt, type: InstitutionType) -> None:
        self.canonical_param: Optional[CourtParam]
        self.param_aliases: list[CourtParam]
        self.code: CourtCode = CourtCode(data["code"])
        self.name: str = data["name"]
        self.grouped_name: str = data.get("grouped_name") or data["name"]
        self.link: str = data["link"]
        self.ncn_pattern: Optional[NeutralCitationPattern] = (
            NeutralCitationPattern(compile(data["ncn_pattern"])) if "ncn_pattern" in data else None
        )
        if "param" in data:
            self.canonical_param = CourtParam(data["param"])
            self.param_aliases = [CourtParam(data["param"])] + [
                CourtParam(extra_param) for extra_param in data.get("extra_params", [])
            ]
        else:
            self.canonical_param = None
            self.param_aliases = []

        self.type = type

        self.start_year: Optional[int] = data.get("start_year")
        self.end_year: int = data.get("end_year") or date.today().year
        self.jurisdictions: list[Jurisdiction] = [
            Jurisdiction(jurisdiction_data) for jurisdiction_data in data.get("jurisdictions", [])
        ]

    def get_jurisdiction(self, code: str) -> Optional[Jurisdiction]:
        return next((j for j in self.jurisdictions if j.code == code), None)

    def expand_jurisdictions(self) -> list["Court"]:
        return [self] + [CourtWithJurisdiction(self, jurisdiction) for jurisdiction in self.jurisdictions]

    def render_markdown_text(self, type: str, context: Dict[str, Any] = {}) -> Optional[str]:
        if not self.canonical_param:
            return None

        filename = self.canonical_param.replace("/", "_")
        description_md_file_path = pathlib.Path(__file__).parent / f"data/markdown/{type}/{filename}.md"
        try:
            with open(description_md_file_path) as file:
                default_context = {"name": self.name, "start_year": self.start_year, "end_year": self.end_year}
                template_context = {**default_context, **context}

                template = file.read()
                template = template.format(**template_context)
                return str(md.render(template))
        except FileNotFoundError:
            return None

    @cached_property
    def description_text_as_html(self) -> Optional[str]:
        """Get the description of the court (where present)."""
        return self.render_markdown_text("description")

    @cached_property
    def historic_documents_support_text_as_html(self) -> Optional[str]:
        """Get support information (where present) on accessing historic court documents not held in FCL."""
        return self.render_markdown_text("historic_docs")

    def __repr__(self) -> str:
        return self.name


class CourtWithJurisdiction(Court):
    def __init__(self, court: Court, jurisdiction: Jurisdiction) -> None:
        self.court: Court = court
        self.jurisdiction: Jurisdiction = jurisdiction
        self.jurisdictions: list[Jurisdiction] = []

    @property
    def code(self) -> CourtCode:
        return CourtCode("/".join((self.court.code, self.jurisdiction.code)))

    @property
    def name(self) -> str:
        return "%s – %s" % (self.court.name, self.jurisdiction.name)

    @property
    def grouped_name(self) -> str:
        return self.court.grouped_name

    @property
    def link(self) -> str:
        return self.court.link

    @property
    def ncn_pattern(self) -> Optional[NeutralCitationPattern]:
        return self.court.ncn_pattern

    @property
    def canonical_param(self) -> Optional[CourtParam]:
        return self.court.canonical_param

    @property
    def param_aliases(self) -> list[CourtParam]:
        return self.court.param_aliases

    @property
    def start_year(self) -> Optional[int]:
        return self.court.start_year

    @property
    def end_year(self) -> int:
        return self.court.end_year

    @property
    def jurisdiction_prefix(self) -> Optional[str]:
        return self.jurisdiction.prefix


class CourtGroup:
    def __init__(self, name: Optional[str], courts: list[Court]) -> None:
        self.name: Optional[str] = name
        self.courts: list[Court] = courts

    @property
    def display_heading(self) -> bool:
        """Is this group displayed in the PUI?"""
        return self.name is not None

    def __repr__(self) -> str:
        return f"CourtGroup({self.name!r}, {self.courts!r})"


class CourtNotFoundException(Exception):
    pass


class CourtsRepository:
    def __init__(self, data: RawCourtRepository):
        self._data: RawCourtRepository = data
        self._byParam: dict[CourtParam, Court] = {}
        self._byCode: dict[CourtCode, Court] = {}
        for group in self._data:
            for courtData in group.get("courts", []):
                court = Court(
                    courtData, type=InstitutionType.TRIBUNAL if group["is_tribunal"] else InstitutionType.COURT
                )
                if "param" in courtData:
                    self._byParam[CourtParam(courtData["param"])] = court
                self._byCode[CourtCode(courtData["code"])] = court

    def __repr__(self) -> str:
        return f"CourtsRepository({self._data!r})"

    def get_by_param(self, param: CourtParam) -> Court:
        try:
            return self._byParam[param]
        except KeyError:
            raise CourtNotFoundException()

    def get_court_by_code(self, code: CourtCode) -> Court:
        try:
            return self._byCode[code]
        except KeyError:
            raise CourtNotFoundException()

    def get_court_with_jurisdiction_by_code(
        self, court_code: CourtCode, jursidiction_code: JurisdictionCode
    ) -> CourtWithJurisdiction:
        court = self.get_court_by_code(court_code)
        if court is None:
            raise CourtNotFoundException()
        jurisdiction = court.get_jurisdiction(jursidiction_code)
        if jurisdiction is None:
            raise CourtNotFoundException()
        return CourtWithJurisdiction(court, jurisdiction)

    def get_by_code(self, code: CourtCode) -> Court:
        if "/" in code:
            (court_code, jurisdiction_code) = code.split("/")
            return self.get_court_with_jurisdiction_by_code(CourtCode(court_code), JurisdictionCode(jurisdiction_code))
        else:
            return self.get_court_by_code(code)

    def get_all(self, with_jurisdictions: bool = False) -> list[Court]:
        courts = [
            Court(court, type=InstitutionType.TRIBUNAL if category["is_tribunal"] else InstitutionType.COURT)
            for category in self._data
            for court in category.get("courts", [])
        ]
        if with_jurisdictions:
            return [c for court in courts for c in court.expand_jurisdictions()]
        else:
            return courts

    def get_selectable(self) -> list[Court]:
        courts = []
        for category in self._data:
            for court in category.get("courts", []):
                if court["selectable"]:
                    courts.append(
                        Court(
                            court, type=InstitutionType.TRIBUNAL if category["is_tribunal"] else InstitutionType.COURT
                        )
                    )
        return courts

    def get_selectable_groups(self) -> list[CourtGroup]:
        groups = []
        for category in self._data:
            courts = [
                Court(court, type=InstitutionType.TRIBUNAL if category["is_tribunal"] else InstitutionType.COURT)
                for court in category.get("courts", [])
                if court["selectable"]
            ]
            if len(courts) > 0:
                groups.append(CourtGroup(category.get("display_name"), courts))
        return groups

    def get_grouped_selectable_courts(self) -> list[CourtGroup]:
        groups = []
        for category in self._data:
            if not category.get("is_tribunal"):
                courts = [
                    Court(court, type=InstitutionType.COURT)
                    for court in category.get("courts", [])
                    if court["selectable"]
                ]
                if len(courts) > 0:
                    groups.append(CourtGroup(category.get("display_name"), courts))
        return groups

    def get_grouped_selectable_tribunals(self) -> list[CourtGroup]:
        groups = []
        for category in self._data:
            if category.get("is_tribunal"):
                courts = [
                    Court(court, InstitutionType.TRIBUNAL)
                    for court in category.get("courts", [])
                    if court["selectable"]
                ]
                if len(courts) > 0:
                    groups.append(CourtGroup(category.get("display_name"), courts))
        return groups

    def get_listable_groups(self) -> list[CourtGroup]:
        groups = []
        for category in self._data:
            courts = [
                Court(court, type=InstitutionType.TRIBUNAL if category["is_tribunal"] else InstitutionType.COURT)
                for court in category.get("courts", [])
                if court["listable"]
            ]
            if len(courts) > 0:
                groups.append(CourtGroup(category.get("display_name"), courts))
        return groups

    def get_listable_courts(self) -> list[Court]:
        courts = []
        for group in self._data:
            if not group.get("is_tribunal"):
                for court in group.get("courts", []):
                    if court["listable"]:
                        courts.append(Court(court, InstitutionType.COURT))
        return courts

    def get_listable_tribunals(self) -> list[Court]:
        courts = []
        for group in self._data:
            if group.get("is_tribunal"):
                for court in group.get("courts", []):
                    if court["listable"]:
                        courts.append(Court(court, InstitutionType.TRIBUNAL))
        return courts


yaml = YAML()
datafile = pathlib.Path(__file__).parent / "data/court_names.yaml"
with open(datafile) as f:
    court_data: RawCourtRepository = yaml.load(f)

courts = CourtsRepository(court_data)
