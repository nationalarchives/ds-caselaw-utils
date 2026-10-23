import typing

from ds_caselaw_utils.courts import Court, InstitutionType
from ds_caselaw_utils.types.courts_schema_autogen import RawCourt, RawCourtRepository


class CourtFactory(Court):
    def __init__(self, data, type=InstitutionType.COURT):
        data = make_court_valid(data, noun=type.value)
        super().__init__(data, type)


def make_court_valid(data, noun="court") -> RawCourt:
    for keyword in ["code", "name", "link"]:
        if keyword not in data:
            data[keyword] = f"placeholder {keyword}"
    if "noun" not in data:
        data["noun"] = noun
    for keyword in ["show_in_search_filters", "show_in_public_directory", "show_to_editors"]:
        if keyword not in data:
            data[keyword] = True

    return typing.cast(RawCourt, data)


def make_court_repo_valid(data) -> RawCourtRepository:
    new_court_groups = []
    for court_group in data:
        new_courts = []
        for court in court_group["courts"]:
            noun = "tribunal" if court_group.get("is_tribunal", False) else "court"
            new_courts.append(make_court_valid(court, noun=noun))
        court_group["court"] = new_courts
        new_court_groups.append(court_group)
    return typing.cast(RawCourtRepository, new_court_groups)
