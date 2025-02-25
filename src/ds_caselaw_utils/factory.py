import typing

from .courts import Court, InstitutionType
from .types.courts_schema_autogen import RawCourt, RawCourtRepository


class CourtFactory(Court):
    def __init__(self, data, type=InstitutionType.COURT):
        data = make_court_valid(data)
        super().__init__(data, type)


def make_court_valid(data) -> RawCourt:
    for keyword in ["code", "name", "link"]:
        if keyword not in data:
            data[keyword] = f"placeholder {keyword}"
    for keyword in ["selectable", "listable"]:
        if keyword not in data:
            data[keyword] = True

    return typing.cast(RawCourt, data)


def make_court_repo_valid(data) -> RawCourtRepository:
    new_court_groups = []
    for court_group in data:
        new_courts = []
        for court in court_group["courts"]:
            new_courts.append(make_court_valid(court))
        court_group["court"] = new_courts
        new_court_groups.append(court_group)
    return typing.cast(RawCourtRepository, new_court_groups)
