import pathlib
import unittest

from ruamel.yaml import YAML

from ds_caselaw_utils.factory import make_court_repo_valid

from .courts import (
    CourtCode,
    CourtGroup,
    CourtNotFoundException,
    CourtParam,
    CourtsRepository,
    InstitutionType,
    courts,
)


class TestCourtsRepository(unittest.TestCase):
    def test_loads_all_courts_without_jurisdictions(self):
        data = [
            {
                "name": "court_group",
                "display_name": "court group 1",
                "is_tribunal": False,
                "courts": [{"name": "court1", "jurisdictions": [{"name": "jurisdiction1", "code": "code"}]}],
            }
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        courts = repo.get_all()
        self.assertIn("court1", [c.name for c in courts])
        self.assertNotIn("court1 – jurisdiction1", [c.name for c in courts])

    def test_loads_all_courts_with_jurisdictions(self):
        data = [
            {
                "name": "court_group",
                "display_name": "court group 1",
                "is_tribunal": False,
                "courts": [{"name": "court1", "jurisdictions": [{"name": "jurisdiction1", "code": "code"}]}],
            }
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        courts = repo.get_all(with_jurisdictions=True)
        self.assertIn("court1", [c.name for c in courts])
        self.assertIn("court1 – jurisdiction1", [c.name for c in courts])

    def test_loads_selectable_courts(self):
        data = [
            {
                "name": "court_group",
                "display_name": "court group 1",
                "is_tribunal": False,
                "courts": [
                    {
                        "name": "court1",
                        "selectable": True,
                    },
                    {"name": "court2", "selectable": False},
                ],
            },
            {
                "name": "court_group2",
                "display_name": "court group 2",
                "is_tribunal": False,
                "courts": [{"name": "court3", "selectable": False}],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        selectable = repo.get_selectable()
        self.assertIn("court1", [c.name for c in selectable])
        self.assertNotIn("court2", [c.name for c in selectable])
        groups = repo.get_selectable_groups()
        self.assertIn("court group 1", [g.name for g in groups])
        self.assertNotIn("court group 2", [g.name for g in groups])
        self.assertIn("court1", [c.name for g in groups for c in g.courts])
        self.assertNotIn("court2", [c.name for g in groups for c in g.courts])
        self.assertNotIn("court3", [c.name for g in groups for c in g.courts])

    def test_loads_listable_courts(self):
        data = [
            {
                "name": "court_group1",
                "display_name": "court group 1",
                "is_tribunal": False,
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
                "is_tribunal": False,
                "courts": [{"name": "court3", "listable": False}],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
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
                "is_tribunal": False,
                "courts": [{"param": "court1", "name": "Court 1"}],
            },
            {
                "name": "court_group2",
                "is_tribunal": False,
                "courts": [{"param": "court2", "name": "Court 2"}],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        self.assertEqual("Court 2", repo.get_by_param(CourtParam("court2")).name)

    def test_raises_on_unknown_court_param(self):
        data = [
            {
                "name": "court_group1",
                "is_tribunal": False,
                "courts": [{"param": "court1", "name": "Court 1"}],
            },
            {
                "name": "court_group2",
                "is_tribunal": False,
                "courts": [{"param": "court2", "name": "Court 2"}],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        self.assertRaises(CourtNotFoundException, repo.get_by_param, "court3")

    def test_loads_court_by_code(self):
        data = [
            {
                "name": "court_group1",
                "is_tribunal": False,
                "courts": [{"code": "court1", "name": "Court 1"}],
            },
            {
                "name": "court_group2",
                "is_tribunal": False,
                "courts": [{"code": "court2", "name": "Court 2"}],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        self.assertEqual("Court 2", repo.get_by_code(CourtCode("court2")).name)

    def test_loads_court_with_jurisdiction_by_code(self):
        data = [
            {
                "name": "court_group",
                "is_tribunal": False,
                "courts": [
                    {
                        "code": "court1",
                        "name": "Court 1",
                        "jurisdictions": [{"code": "jurisdiction1", "name": "Jurisdiction 1"}],
                    }
                ],
            }
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        self.assertEqual("Court 1 – Jurisdiction 1", repo.get_by_code(CourtCode("court1/jurisdiction1")).name)

    def test_raises_error_for_nonexistent_jurisdictions(self):
        data = [
            {
                "name": "court_group",
                "is_tribunal": False,
                "courts": [
                    {
                        "code": "court1",
                        "name": "Court 1",
                        "jurisdictions": [{"code": "jurisdiction1", "name": "Jurisdiction 1"}],
                    }
                ],
            }
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        self.assertRaises(CourtNotFoundException, repo.get_by_code, "court1/jurisdiction2")
        self.assertRaises(CourtNotFoundException, repo.get_by_code, "court2/jurisdiction1")

    def test_raises_on_unknown_court_code(self):
        data = [
            {
                "name": "court_group1",
                "is_tribunal": False,
                "courts": [{"code": "court1", "name": "Court 1"}],
            },
            {
                "name": "court_group2",
                "is_tribunal": False,
                "courts": [{"code": "court2", "name": "Court 2"}],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        self.assertRaises(CourtNotFoundException, repo.get_by_code, "court3")

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
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        self.assertIn("court1", [c.canonical_param for c in repo.get_listable_courts()])
        self.assertNotIn("court2", [c.canonical_param for c in repo.get_listable_courts()])
        self.assertNotIn("court3", [c.canonical_param for c in repo.get_listable_courts()])

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
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        self.assertNotIn("court1", [c.canonical_param for c in repo.get_listable_tribunals()])
        self.assertNotIn("court2", [c.canonical_param for c in repo.get_listable_tribunals()])
        self.assertIn("court3", [c.canonical_param for c in repo.get_listable_tribunals()])

    def test_returns_grouped_selectable_courts(self):
        data = [
            {
                "name": "group2",
                "display_name": "Court group",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "selectable": True, "name": "Selectable court"},
                    {
                        "param": "court2",
                        "selectable": False,
                        "name": "Unselectable court",
                    },
                ],
            },
            {
                "name": "group2",
                "display_name": "Tribunal group",
                "is_tribunal": True,
                "courts": [
                    {
                        "param": "court3",
                        "selectable": True,
                        "name": "Selectable tribunal",
                    }
                ],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        groups = repo.get_grouped_selectable_courts()
        self.assertIn("Court group", [g.name for g in groups])
        self.assertNotIn("Tribunal group", [g.name for g in groups])
        self.assertIn("Selectable court", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Unselectable court", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Selectable tribunal", [c.name for g in groups for c in g.courts])

    def test_returns_grouped_selectable_tribunals(self):
        data = [
            {
                "name": "group1",
                "display_name": "Court group",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "selectable": True, "name": "Selectable court"},
                ],
            },
            {
                "name": "group2",
                "display_name": "Tribunal group",
                "is_tribunal": True,
                "courts": [
                    {
                        "param": "court2",
                        "selectable": True,
                        "name": "Selectable tribunal",
                    },
                    {
                        "param": "court3",
                        "selectable": False,
                        "name": "Unselectable tribunal",
                    },
                ],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        groups = repo.get_grouped_selectable_tribunals()
        self.assertIn("Tribunal group", [g.name for g in groups])
        self.assertNotIn("Court group", [g.name for g in groups])
        self.assertIn("Selectable tribunal", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Unselectable tribunal", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Selectable court", [c.name for g in groups for c in g.courts])

    def test_repr(self):
        data = [
            {
                "name": "group1",
                "display_name": "Court group",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "selectable": True, "name": "Selectable court"},
                ],
            }
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        assert "'name': 'group1', 'display_name': 'Court group'" in str(repo)

    def test_identifies_institution_type(self):
        data = [
            {
                "name": "courts",
                "is_tribunal": False,
                "courts": [
                    {"param": "court", "listable": True, "name": "Court"},
                ],
            },
            {
                "name": "tribunals",
                "is_tribunal": True,
                "courts": [
                    {"param": "tribunal", "listable": True, "name": "Tribunal"},
                ],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        institutions = repo.get_all()

        assert institutions[0].type is InstitutionType.COURT
        assert institutions[1].type is InstitutionType.TRIBUNAL


class TestCourtGroup(unittest.TestCase):
    def test_display_heading_when_has_display_name(self):
        group = CourtGroup("name", [])
        assert group.display_heading

    def test_dont_display_heading_when_no_display_name(self):
        group = CourtGroup(None, [])
        assert not group.display_heading

    def test_repr(self):
        group = CourtGroup("name", [])
        assert str(group) == "CourtGroup('name', [])"


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


class TestAutogenCourtsJson(unittest.TestCase):
    def test_autogen_courts_json(self):
        """Check that one edge case is handled correctly in the autogenerated JSON"""
        datafile = datafile = pathlib.Path(__file__).parent.parent.parent / "src/autogen/courts.json"
        with open(datafile) as f:
            raw_json = f.read()
        assert '"identifier_iri": "http://www.tribunals.gov.uk/ImmigrationAsylum/"' in raw_json
