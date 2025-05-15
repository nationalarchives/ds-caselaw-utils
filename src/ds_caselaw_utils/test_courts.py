import pathlib
import unittest
from datetime import date
from unittest.mock import MagicMock, PropertyMock, mock_open, patch

from ruamel.yaml import YAML

from ds_caselaw_utils.factory import CourtFactory, make_court_repo_valid

from .courts import (
    Court,
    CourtCode,
    CourtGroup,
    CourtNotFoundException,
    CourtParam,
    CourtsRepository,
    CourtWithJurisdiction,
    InstitutionType,
    courts,
)


def mock_with_properties(properties={}):
    mock = MagicMock()
    for property, value in properties.items():
        property_mock = PropertyMock(return_value=value)
        setattr(type(mock), property, property_mock)
        setattr(mock, "mock_%s" % property, property_mock)
    return mock


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


class TestCourt(unittest.TestCase):
    def test_repr_string(self):
        court = CourtFactory({"name": "court_name"})
        self.assertEqual("court_name", str(court))
        self.assertEqual("court_name", repr(court))

    def test_grouped_name_explicit(self):
        court = CourtFactory({"grouped_name": "court_name"})
        self.assertEqual("court_name", court.grouped_name)

    def test_grouped_name_default(self):
        court = CourtFactory({"name": "court_name"})
        self.assertEqual("court_name", court.grouped_name)

    def test_param_aliases(self):
        court = CourtFactory({"param": "param_1", "extra_params": ["param_2"]})
        self.assertEqual(["param_1", "param_2"], court.param_aliases)

    def test_end_year_explicit(self):
        court = CourtFactory({"end_year": 1983})
        self.assertEqual(1983, court.end_year)

    def test_end_year_default(self):
        court = CourtFactory({})
        self.assertEqual(date.today().year, court.end_year)

    def test_type_when_court(self):
        court = CourtFactory({})
        assert court.type is InstitutionType.COURT

    def test_type_when_tribunal(self):
        court = CourtFactory({}, type=InstitutionType.TRIBUNAL)
        assert court.type is InstitutionType.TRIBUNAL

    def test_get_jurisdiction(self):
        court = CourtFactory({"jurisdictions": [{"code": "jurisdiction1", "name": "Jurisdiction 1"}]})
        jurisdiction = court.get_jurisdiction("jurisdiction1")
        assert jurisdiction
        self.assertEqual("Jurisdiction 1", jurisdiction.name)

    def test_get_nonexistent_jurisdiction(self):
        court = CourtFactory({"jurisdictions": [{"code": "jurisdiction1", "name": "Jurisdiction 1"}]})
        jurisdiction = court.get_jurisdiction("jurisdiction2")
        self.assertIsNone(jurisdiction)

    def test_expand_jurisdictions(self):
        court = CourtFactory(
            {
                "name": "Court 1",
                "jurisdictions": [{"code": "jurisdiction1", "name": "Jurisdiction 1"}],
            }
        )
        expanded = court.expand_jurisdictions()
        self.assertIn("Court 1", [c.name for c in expanded])
        self.assertIn("Court 1 – Jurisdiction 1", [c.name for c in expanded])
        for c in expanded:
            assert issubclass(type(c), Court)

    def test_render_markdown_text_if_no_canonical_param(self):
        court = CourtFactory({"param": "test"})
        assert court.description_text_as_html is None

    def test_render_markdown_text_if_no_file(self):
        court = CourtFactory({"param": "test"})
        assert court.description_text_as_html is None

    def test_render_markdown_text_if_file(self):
        court = CourtFactory({"param": "test"})
        with patch("pathlib.Path.is_file", True), patch("builtins.open", mock_open(read_data="**Test** description.")):
            assert court.render_markdown_text("test") == "<p><strong>Test</strong> description.</p>\n"

    def test_render_markdown_text_with_context(self):
        court = CourtFactory({"param": "test", "name": "test name", "start_year": 2000, "end_year": 2025})
        with (
            patch("pathlib.Path.is_file", True),
            patch(
                "builtins.open",
                mock_open(
                    read_data="**Test** description.\n - Name: {name}\n - Start year: {start_year}\n - End year: {end_year}"
                ),
            ),
        ):
            assert (
                court.render_markdown_text("test")
                == "<p><strong>Test</strong> description.</p>\n<ul>\n<li>Name: test name</li>\n<li>Start year: 2000</li>\n<li>End year: 2025</li>\n</ul>\n"
            )

    @patch("ds_caselaw_utils.courts.Court.render_markdown_text")
    def test_description_text_as_html(self, mock_render):
        court = CourtFactory({"param": "test"})
        mock_render.return_value = "<p>Description.</p>"

        assert court.description_text_as_html == "<p>Description.</p>"
        mock_render.assert_called_once_with("description")

    @patch("ds_caselaw_utils.courts.Court.render_markdown_text")
    def test_historic_documents_support_text_as_html(self, mock_render):
        court = CourtFactory({"param": "test"})
        mock_render.return_value = "<p>Support text.</p>"

        assert court.historic_documents_support_text_as_html == "<p>Support text.</p>"
        mock_render.assert_called_once_with("historic_docs")


class TestCourtWithJurisdiction(unittest.TestCase):
    def test_code(self):
        # It appends the jurisdiction code to the court code
        # separated with a slash
        court = mock_with_properties({"code": "court_code"})
        jurisdiction = mock_with_properties({"code": "jurisdiction_code"})
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.code, "court_code/jurisdiction_code")
        court.mock_code.assert_called()
        jurisdiction.mock_code.assert_called()

    def test_name(self):
        # It appends the jurisdiction name to the court name
        # separated with an en-dash
        court = mock_with_properties({"name": "court_name"})
        jurisdiction = mock_with_properties({"name": "jurisdiction_name"})
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.name, "court_name – jurisdiction_name")
        court.mock_name.assert_called()
        jurisdiction.mock_name.assert_called()

    def test_grouped_name(self):
        # It returns the court grouped name
        court = mock_with_properties({"grouped_name": "court_grouped_name"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.grouped_name, "court_grouped_name")
        court.mock_grouped_name.assert_called()

    def test_link(self):
        # It returns the court link
        court = mock_with_properties({"link": "court_link"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.link, "court_link")
        court.mock_link.assert_called()

    def test_ncn_pattern(self):
        # It returns the court's NCN pattern
        court = mock_with_properties({"ncn_pattern": "court_ncn"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.ncn_pattern, "court_ncn")
        court.mock_ncn_pattern.assert_called()

    def test_canonical_param(self):
        # It returns the court canonical_param
        court = mock_with_properties({"canonical_param": "court_canonical_param"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.canonical_param, "court_canonical_param")
        court.mock_canonical_param.assert_called()

    def param_aliases(self):
        # It returns the court param_aliases
        court = mock_with_properties({"param_aliases": "court_param_aliases"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.param_aliases, "court_param_aliases")
        court.mock_param_aliases.assert_called()

    def start_year(self):
        # It returns the court start_year
        court = mock_with_properties({"start_year": "court_start_year"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.start_year, "court_start_year")
        court.mock_start_year.assert_called()

    def end_year(self):
        # It returns the court end_year
        court = mock_with_properties({"end_year": "court_end_year"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.end_year, "court_end_year")
        court.mock_end_year.assert_called()

    def test_jurisdiction_prefix(self):
        # It returns the jurisdiction prefix:
        court = mock_with_properties()
        jurisdiction = mock_with_properties({"prefix": "ABC"})
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.jurisdiction_prefix, "ABC")
        jurisdiction.mock_prefix.assert_called()


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
