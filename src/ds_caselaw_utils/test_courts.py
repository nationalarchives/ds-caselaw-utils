import pathlib
import unittest
from datetime import date

from ruamel.yaml import YAML

from .courts import Court, CourtsRepository, courts


class TestCourtsRepository(unittest.TestCase):
    def test_loads_selectable_courts(self):
        data = [
            {
                "name": "court_group",
                "courts": [
                    {
                        "name": "court1",
                        "selectable": True,
                    },
                    {"name": "court2", "selectable": False},
                ],
            }
        ]
        repo = CourtsRepository(data)
        selectable = repo.get_selectable()
        self.assertIn("court1", [c.name for c in selectable])
        self.assertNotIn("court2", [c.name for c in selectable])

    def test_loads_listable_courts(self):
        data = [
            {
                "name": "court_group1",
                "display_name": "court group 1",
                "courts": [
                    {
                        "name": "court1",
                        "listable": True,
                    },
                    {"name": "court2", "listable": False},
                ],
            },
            {
                "name": "court_group2",
                "display_name": "court group 2",
                "courts": [{"name": "court3", "listable": False}],
            },
        ]
        repo = CourtsRepository(data)
        groups = repo.get_listable_groups()
        self.assertIn("court group 1", [g.name for g in groups])
        self.assertNotIn("court group 2", [g.name for g in groups])
        self.assertIn("court1", [c.name for g in groups for c in g.courts])
        self.assertNotIn("court2", [c.name for g in groups for c in g.courts])
        self.assertNotIn("court3", [c.name for g in groups for c in g.courts])

    def test_loads_court_by_param(self):
        data = [
            {
                "name": "court_group1",
                "courts": [{"param": "court1", "name": "Court 1"}],
            },
            {
                "name": "court_group2",
                "courts": [{"param": "court2", "name": "Court 2"}],
            },
        ]
        repo = CourtsRepository(data)
        self.assertEqual("Court 2", repo.get_by_param("court2").name)

    def test_loads_court_by_code(self):
        data = [
            {
                "name": "court_group1",
                "courts": [{"code": "court1", "name": "Court 1"}],
            },
            {
                "name": "court_group2",
                "courts": [{"code": "court2", "name": "Court 2"}],
            },
        ]
        repo = CourtsRepository(data)
        self.assertEqual("Court 2", repo.get_by_code("court2").name)

    def test_returns_listable_courts(self):
        data = [
            {
                "name": "court_group1",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "listable": True, "name": "Court 1"},
                    {"param": "court2", "listable": False, "name": "Court 2"},
                ],
            },
            {
                "name": "court_group2",
                "is_tribunal": True,
                "courts": [{"param": "court3", "listable": True, "name": "Court 3"}],
            },
        ]
        repo = CourtsRepository(data)
        self.assertIn("court1", [c.canonical_param for c in repo.get_listable_courts()])
        self.assertNotIn(
            "court2", [c.canonical_param for c in repo.get_listable_courts()]
        )
        self.assertNotIn(
            "court3", [c.canonical_param for c in repo.get_listable_courts()]
        )

    def test_returns_listable_tribunals(self):
        data = [
            {
                "name": "court_group1",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "listable": True, "name": "Court 1"},
                ],
            },
            {
                "name": "court_group2",
                "is_tribunal": True,
                "courts": [
                    {"param": "court2", "listable": False, "name": "Court 2"},
                    {"param": "court3", "listable": True, "name": "Court 3"},
                ],
            },
        ]
        repo = CourtsRepository(data)
        self.assertNotIn(
            "court1", [c.canonical_param for c in repo.get_listable_tribunals()]
        )
        self.assertNotIn(
            "court2", [c.canonical_param for c in repo.get_listable_tribunals()]
        )
        self.assertIn(
            "court3", [c.canonical_param for c in repo.get_listable_tribunals()]
        )


class TestCourt(unittest.TestCase):
    def test_list_name_explicit(self):
        court = Court({"list_name": "court_name"})
        self.assertEqual("court_name", court.list_name)

    def test_list_name_default(self):
        court = Court({"name": "court_name"})
        self.assertEqual("court_name", court.list_name)

    def test_param_aliases(self):
        court = Court({"param": "param_1", "extra_params": ["param_2"]})
        self.assertEqual(["param_1", "param_2"], court.param_aliases)

    def test_end_year_explicit(self):
        court = Court({"end_year": 1983})
        self.assertEqual(1983, court.end_year)

    def test_end_year_default(self):
        court = Court({})
        self.assertEqual(date.today().year, court.end_year)


class TestCourts(unittest.TestCase):
    def test_loads_court_yaml(self):
        yaml = YAML()
        datafile = pathlib.Path(__file__).parent / "data/court_names.yaml"
        with open(datafile) as f:
            court_data = yaml.load(f)
        courts_from_yaml = []
        for group in court_data:
            for court in group.get("courts"):
                courts_from_yaml.append(court)
        for court, data in zip(courts.get_all(), courts_from_yaml):
            self.assertEqual(court.name, data["name"])
