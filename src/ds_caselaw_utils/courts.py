"""
Get metada data for the courts covered by the service
"""

import pathlib
from datetime import date

from ruamel.yaml import YAML


class Jurisdiction:
    def __init__(self, data):
        self.code = data.get("code")
        self.name = data.get("name")
        self.prefix = data.get("prefix")


class Court:
    def __init__(self, data):
        self.code = data.get("code")
        self.name = data.get("name")
        self.grouped_name = data.get("grouped_name") or data.get("name")
        self.link = data.get("link")
        self.ncn = data.get("ncn")
        self.canonical_param = data.get("param")
        self.param_aliases = [data.get("param")] + (data.get("extra_params") or [])
        self.start_year = data.get("start_year")
        self.end_year = data.get("end_year") or date.today().year
        self.jurisdictions = [Jurisdiction(jurisdiction_data) for jurisdiction_data in data.get("jurisdictions", [])]

    def get_jurisdiction(self, code):
        return next((j for j in self.jurisdictions if j.code == code), None)

    def expand_jurisdictions(self):
        return [self] + [CourtWithJurisdiction(self, jurisdiction) for jurisdiction in self.jurisdictions]

    def __repr__(self):
        return self.name


class CourtWithJurisdiction(Court):
    def __init__(self, court, jurisdiction):
        self.court = court
        self.jurisdiction = jurisdiction
        self.jurisdictions = []

    @property
    def code(self):
        return "/".join((self.court.code, self.jurisdiction.code))

    @property
    def name(self):
        return "%s – %s" % (self.court.name, self.jurisdiction.name)

    @property
    def grouped_name(self):
        return self.court.grouped_name

    @property
    def link(self):
        return self.court.link

    @property
    def ncn(self):
        return self.court.ncn

    @property
    def canonical_param(self):
        return self.court.canonical_param

    @property
    def param_aliases(self):
        return self.court.param_aliases

    @property
    def start_year(self):
        return self.court.start_year

    @property
    def end_year(self):
        return self.court.end_year

    @property
    def jurisdiction_prefix(self):
        return self.jurisdiction.prefix


class CourtGroup:
    def __init__(self, name, courts):
        self.name = name
        self.courts = courts

    @property
    def display_heading(self):
        return self.name is not None


class CourtNotFoundException(Exception):
    pass


class CourtsRepository:
    def __init__(self, data):
        self._data = data
        self._byParam = {}
        self._byCode = {}
        for group in self._data:
            for courtData in group.get("courts"):
                court = Court(courtData)
                self._byParam[courtData.get("param")] = court
                self._byCode[courtData.get("code")] = court

    def get_by_param(self, param):
        try:
            return self._byParam[param]
        except KeyError:
            raise CourtNotFoundException()

    def get_court_by_code(self, code):
        try:
            return self._byCode[code]
        except KeyError:
            raise CourtNotFoundException()

    def get_court_with_jurisdiction_by_code(self, court_code, jursidiction_code):
        court = self.get_court_by_code(court_code)
        if court is None:
            raise CourtNotFoundException()
        jurisdiction = court.get_jurisdiction(jursidiction_code)
        if jurisdiction is None:
            raise CourtNotFoundException()
        return CourtWithJurisdiction(court, jurisdiction)

    def get_by_code(self, code):
        if "/" in code:
            (court_code, jurisdiction_code) = code.split("/")
            return self.get_court_with_jurisdiction_by_code(court_code, jurisdiction_code)
        else:
            return self.get_court_by_code(code)

    def get_all(self, with_jurisdictions=False):
        courts = [Court(court) for category in self._data for court in category.get("courts")]
        if with_jurisdictions:
            return [c for court in courts for c in court.expand_jurisdictions()]
        else:
            return courts

    def get_selectable(self):
        courts = []
        for category in self._data:
            for court in category.get("courts"):
                if court.get("selectable"):
                    courts.append(Court(court))
        return courts

    def get_selectable_groups(self):
        groups = []
        for category in self._data:
            courts = [Court(court) for court in category.get("courts") if court.get("selectable")]
            if len(courts) > 0:
                groups.append(CourtGroup(category.get("display_name"), courts))
        return groups

    def get_grouped_selectable_courts(self):
        groups = []
        for category in self._data:
            if not category.get("is_tribunal"):
                courts = [Court(court) for court in category.get("courts") if court.get("selectable")]
                if len(courts) > 0:
                    groups.append(CourtGroup(category.get("display_name"), courts))
        return groups

    def get_grouped_selectable_tribunals(self):
        groups = []
        for category in self._data:
            if category.get("is_tribunal"):
                courts = [Court(court) for court in category.get("courts") if court.get("selectable")]
                if len(courts) > 0:
                    groups.append(CourtGroup(category.get("display_name"), courts))
        return groups

    def get_listable_groups(self):
        groups = []
        for category in self._data:
            courts = [Court(court) for court in category.get("courts") if court.get("listable")]
            if len(courts) > 0:
                groups.append(CourtGroup(category.get("display_name"), courts))
        return groups

    def get_listable_courts(self):
        courts = []
        for group in self._data:
            if not group.get("is_tribunal"):
                for court in group.get("courts", []):
                    if court.get("listable"):
                        courts.append(Court(court))
        return courts

    def get_listable_tribunals(self):
        courts = []
        for group in self._data:
            if group.get("is_tribunal"):
                for court in group.get("courts", []):
                    if court.get("listable"):
                        courts.append(Court(court))
        return courts


yaml = YAML()
datafile = pathlib.Path(__file__).parent / "data/court_names.yaml"
with open(datafile) as f:
    court_data = yaml.load(f)

courts = CourtsRepository(court_data)
