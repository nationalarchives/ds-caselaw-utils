import pathlib
import unittest

from ruamel.yaml import YAML

from ds_caselaw_utils.courts import (
    CourtCode,
    CourtGroup,
    CourtNotFoundException,
    CourtParam,
    CourtsRepository,
    InstitutionType,
    courts,
)
from ds_caselaw_utils.tests.factory import make_court_repo_valid


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

    def test_loads_show_in_search_filters_courts(self):
        data = [
            {
                "name": "court_group",
                "display_name": "court group 1",
                "is_tribunal": False,
                "courts": [
                    {
                        "name": "court1",
                        "show_in_search_filters": True,
                    },
                    {"name": "court2", "show_in_search_filters": False},
                ],
            },
            {
                "name": "court_group2",
                "display_name": "court group 2",
                "is_tribunal": False,
                "courts": [{"name": "court3", "show_in_search_filters": False}],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        show_in_search_filters = repo.get_show_in_search_filters()
        self.assertIn("court1", [c.name for c in show_in_search_filters])
        self.assertNotIn("court2", [c.name for c in show_in_search_filters])
        groups = repo.get_show_in_search_filters_groups()
        self.assertIn("court group 1", [g.name for g in groups])
        self.assertNotIn("court group 2", [g.name for g in groups])
        self.assertIn("court1", [c.name for g in groups for c in g.courts])
        self.assertNotIn("court2", [c.name for g in groups for c in g.courts])
        self.assertNotIn("court3", [c.name for g in groups for c in g.courts])

    def test_loads_show_in_public_directory_courts(self):
        data = [
            {
                "name": "court_group",
                "display_name": "court group 1",
                "is_tribunal": False,
                "courts": [
                    {
                        "name": "court1",
                        "show_in_public_directory": True,
                    },
                    {"name": "court2", "show_in_public_directory": False},
                ],
            },
            {
                "name": "court_group2",
                "display_name": "court group 2",
                "is_tribunal": False,
                "courts": [{"name": "court3", "show_in_public_directory": False}],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        show_in_public_directory = repo.get_show_in_public_directory()
        self.assertIn("court1", [c.name for c in show_in_public_directory])
        self.assertNotIn("court2", [c.name for c in show_in_public_directory])
        groups = repo.get_show_in_public_directory_groups()
        self.assertIn("court group 1", [g.name for g in groups])
        self.assertNotIn("court group 2", [g.name for g in groups])
        self.assertIn("court1", [c.name for g in groups for c in g.courts])
        self.assertNotIn("court2", [c.name for g in groups for c in g.courts])
        self.assertNotIn("court3", [c.name for g in groups for c in g.courts])

    def test_loads_show_to_editors_courts(self):
        data = [
            {
                "name": "court_group1",
                "display_name": "court group 1",
                "is_tribunal": False,
                "courts": [
                    {
                        "name": "court1",
                        "show_to_editors": True,
                    },
                    {"name": "court2", "show_to_editors": False},
                ],
            },
            {
                "name": "court_group2",
                "display_name": "court group 2",
                "is_tribunal": False,
                "courts": [{"name": "court3", "show_to_editors": False}],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        groups = repo.get_show_to_editors_groups()
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

    def test_returns_show_to_editors_courts(self):
        data = [
            {
                "name": "court_group1",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "show_to_editors": True, "name": "Court 1"},
                    {"param": "court2", "show_to_editors": False, "name": "Court 2"},
                ],
            },
            {
                "name": "court_group2",
                "is_tribunal": True,
                "courts": [{"param": "court3", "show_to_editors": True, "name": "Court 3"}],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        self.assertIn("court1", [c.canonical_param for c in repo.get_show_to_editors_courts()])
        self.assertNotIn("court2", [c.canonical_param for c in repo.get_show_to_editors_courts()])
        self.assertNotIn("court3", [c.canonical_param for c in repo.get_show_to_editors_courts()])

    def test_returns_show_to_editors_tribunals(self):
        data = [
            {
                "name": "court_group1",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "show_to_editors": True, "name": "Court 1"},
                ],
            },
            {
                "name": "court_group2",
                "is_tribunal": True,
                "courts": [
                    {"param": "court2", "show_to_editors": False, "name": "Court 2"},
                    {"param": "court3", "show_to_editors": True, "name": "Court 3"},
                ],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        self.assertNotIn("court1", [c.canonical_param for c in repo.get_show_to_editors_tribunals()])
        self.assertNotIn("court2", [c.canonical_param for c in repo.get_show_to_editors_tribunals()])
        self.assertIn("court3", [c.canonical_param for c in repo.get_show_to_editors_tribunals()])

    def test_returns_grouped_show_in_search_filters_courts(self):
        data = [
            {
                "name": "group2",
                "display_name": "Court group",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "show_in_search_filters": True, "name": "Show in search filters court"},
                    {
                        "param": "court2",
                        "show_in_search_filters": False,
                        "name": "Hidden in search filters court",
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
                        "show_in_search_filters": True,
                        "name": "Show in search filters tribunal",
                    }
                ],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        groups = repo.get_grouped_show_in_search_filters_courts()
        self.assertIn("Court group", [g.name for g in groups])
        self.assertNotIn("Tribunal group", [g.name for g in groups])
        self.assertIn("Show in search filters court", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Hidden in search filters court", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Show in search filters tribunal", [c.name for g in groups for c in g.courts])

    def test_returns_grouped_show_in_search_filters_tribunals(self):
        data = [
            {
                "name": "group1",
                "display_name": "Court group",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "show_in_search_filters": True, "name": "Show in search filters court"},
                ],
            },
            {
                "name": "group2",
                "display_name": "Tribunal group",
                "is_tribunal": True,
                "courts": [
                    {
                        "param": "court2",
                        "show_in_search_filters": True,
                        "name": "Show in search filters tribunal",
                    },
                    {
                        "param": "court3",
                        "show_in_search_filters": False,
                        "name": "Hidden in search filters tribunal",
                    },
                ],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        groups = repo.get_grouped_show_in_search_filters_tribunals()
        self.assertIn("Tribunal group", [g.name for g in groups])
        self.assertNotIn("Court group", [g.name for g in groups])
        self.assertIn("Show in search filters tribunal", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Hidden in search filters tribunal", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Show in search filters court", [c.name for g in groups for c in g.courts])

    def test_returns_grouped_show_in_public_directory_courts(self):
        data = [
            {
                "name": "group2",
                "display_name": "Court group",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "show_in_public_directory": True, "name": "Show in public directory court"},
                    {
                        "param": "court2",
                        "show_in_public_directory": False,
                        "name": "Hidden from public directory court",
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
                        "show_in_public_directory": True,
                        "name": "Show in public directory tribunal",
                    }
                ],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        groups = repo.get_grouped_show_in_public_directory_courts()
        self.assertIn("Court group", [g.name for g in groups])
        self.assertNotIn("Tribunal group", [g.name for g in groups])
        self.assertIn("Show in public directory court", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Hidden from public directory court", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Show in public directory tribunal", [c.name for g in groups for c in g.courts])

    def test_returns_grouped_show_in_public_directory_tribunals(self):
        data = [
            {
                "name": "group1",
                "display_name": "Court group",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "show_in_public_directory": True, "name": "Show in public directory court"},
                ],
            },
            {
                "name": "group2",
                "display_name": "Tribunal group",
                "is_tribunal": True,
                "courts": [
                    {
                        "param": "court2",
                        "show_in_public_directory": True,
                        "name": "Show in public directory tribunal",
                    },
                    {
                        "param": "court3",
                        "show_in_public_directory": False,
                        "name": "Hidden from public directory tribunal",
                    },
                ],
            },
        ]
        valid_data = make_court_repo_valid(data)
        repo = CourtsRepository(valid_data)
        groups = repo.get_grouped_show_in_public_directory_tribunals()
        self.assertIn("Tribunal group", [g.name for g in groups])
        self.assertNotIn("Court group", [g.name for g in groups])
        self.assertIn("Show in public directory tribunal", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Hidden from public directory tribunal", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Show in public directory court", [c.name for g in groups for c in g.courts])

    def test_returns_grouped_show_to_editors_courts(self):
        data = [
            {
                "name": "group1",
                "display_name": "Court group",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "show_to_editors": True, "name": "Show to editors court"},
                    {"param": "court2", "show_to_editors": False, "name": "Hidden from editors court"},
                ],
            },
            {
                "name": "group2",
                "display_name": "Tribunal group",
                "is_tribunal": True,
                "courts": [{"param": "court3", "show_to_editors": True, "name": "Show to editors tribunal"}],
            },
        ]
        repo = CourtsRepository(make_court_repo_valid(data))
        groups = repo.get_grouped_show_to_editors_courts()
        self.assertIn("Court group", [g.name for g in groups])
        self.assertNotIn("Tribunal group", [g.name for g in groups])
        self.assertIn("Show to editors court", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Hidden from editors court", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Show to editors tribunal", [c.name for g in groups for c in g.courts])

    def test_returns_grouped_show_to_editors_tribunals(self):
        data = [
            {
                "name": "group1",
                "display_name": "Court group",
                "is_tribunal": False,
                "courts": [{"param": "court1", "show_to_editors": True, "name": "Show to editors court"}],
            },
            {
                "name": "group2",
                "display_name": "Tribunal group",
                "is_tribunal": True,
                "courts": [
                    {"param": "court2", "show_to_editors": True, "name": "Show to editors tribunal"},
                    {"param": "court3", "show_to_editors": False, "name": "Hidden from editors tribunal"},
                ],
            },
        ]
        repo = CourtsRepository(make_court_repo_valid(data))
        groups = repo.get_grouped_show_to_editors_tribunals()
        self.assertIn("Tribunal group", [g.name for g in groups])
        self.assertNotIn("Court group", [g.name for g in groups])
        self.assertIn("Show to editors tribunal", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Hidden from editors tribunal", [c.name for g in groups for c in g.courts])
        self.assertNotIn("Show to editors court", [c.name for g in groups for c in g.courts])

    def test_repr(self):
        data = [
            {
                "name": "group1",
                "display_name": "Court group",
                "is_tribunal": False,
                "courts": [
                    {"param": "court1", "show_in_search_filters": True, "name": "Show in search filters court"},
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
                    {"param": "court", "show_to_editors": True, "name": "Court"},
                ],
            },
            {
                "name": "tribunals",
                "is_tribunal": True,
                "courts": [
                    {"param": "tribunal", "show_to_editors": True, "name": "Tribunal"},
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
        datafile = pathlib.Path(__file__).parent.parent / "data/court_names.yaml"
        with open(datafile) as f:
            court_data = yaml.load(f)
        courts_from_yaml = [court for group in court_data for court in group.get("courts")]
        for court, data in zip(courts.get_all(), courts_from_yaml):
            self.assertEqual(court.name, data["name"])


class TestAutogenCourtsJson(unittest.TestCase):
    def test_autogen_courts_json(self):
        """Check that one edge case is handled correctly in the autogenerated JSON"""
        datafile = pathlib.Path(__file__).parent.parent.parent.parent / "src/autogen/courts.json"
        with open(datafile) as f:
            raw_json = f.read()
        assert '"identifier_iri": "http://www.tribunals.gov.uk/ImmigrationAsylum/"' in raw_json
