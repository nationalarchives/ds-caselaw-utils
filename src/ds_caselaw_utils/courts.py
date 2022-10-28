"""
Get metada data for the courts covered by the service
"""

import pathlib
from datetime import date

from ruamel.yaml import YAML


class Court:
    def __init__(self, data):
        self.code = data.get("code")
        self.name = data.get("name")
        self.list_name = data.get("list_name") or data.get("name")
        self.link = data.get("link")
        self.ncn = data.get("ncn")
        self.canonical_param = data.get("param")
        self.param_aliases = [data.get("param")] + (data.get("extra_params") or [])
        self.start_year = data.get("start_year")
        self.end_year = data.get("end_year") or date.today().year


class CourtGroup:
    def __init__(self, name, courts):
        self.name = name
        self.courts = courts


class CourtsRepository:
    def __init__(self, data):
        self._data = data

    def get_by_param(self, param):
        for group in self._data:
            for court in group.get("courts"):
                if court.get("param") == param:
                    return Court(court)

    def get_all(self):
        return [
            Court(court) for category in self._data for court in category.get("courts")
        ]

    def get_selectable(self):
        courts = []
        for category in self._data:
            for court in category.get("courts"):
                if court.get("selectable"):
                    courts.append(Court(court))
        return courts

    def get_listable_groups(self):
        groups = []
        for category in self._data:
            courts = [
                Court(court)
                for court in category.get("courts")
                if court.get("listable")
            ]
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
