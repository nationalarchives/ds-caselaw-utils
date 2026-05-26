import unittest
from datetime import date
from unittest.mock import MagicMock, PropertyMock, mock_open, patch

from ds_caselaw_utils.courts import (
    Court,
    CourtWithJurisdiction,
    InstitutionType,
)
from ds_caselaw_utils.tests.factory import CourtFactory


def mock_with_properties(properties={}):
    mock = MagicMock(spec=dict)
    for property, value in properties.items():
        property_mock = PropertyMock(return_value=value)
        setattr(type(mock), property, property_mock)
        setattr(mock, "mock_%s" % property, property_mock)
    return mock


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
        court = CourtFactory({})
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
                    read_data="**Test** description.\n - Name: {name}\n - Start year: {start_year}\n - End year: {end_year}\n - Do not replace: {do_not_replace}"
                ),
            ),
        ):
            assert (
                court.render_markdown_text("test")
                == "<p><strong>Test</strong> description.</p>\n<ul>\n<li>Name: test name</li>\n<li>Start year: 2000</li>\n<li>End year: 2025</li>\n<li>Do not replace: {do_not_replace}</li>\n</ul>\n"
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

    def test_link_and_iri_with_default_iri(self):
        # It returns the court link
        court = CourtFactory({"link": "court_link"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.link, "court_link")
        self.assertEqual(cwj.identifier_iri, "court_link")

    def test_link_and_iri_with_custom_iri(self):
        # It returns the court link
        court = CourtFactory({"link": "court_link", "identifier_iri": "court_identifier_iri"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.link, "court_link")
        self.assertEqual(cwj.identifier_iri, "court_identifier_iri")

    def test_ncn_pattern(self):
        # It returns the court's NCN pattern
        court = mock_with_properties({"ncn_pattern": "court_ncn"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.ncn_pattern, "court_ncn")
        court.mock_ncn_pattern.assert_called()

    def test_ncn_examples(self):
        # It returns the court's NCN examples
        court = mock_with_properties({"ncn_examples": ["[2025] UKSC 123"]})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.ncn_examples, ["[2025] UKSC 123"])
        court.mock_ncn_examples.assert_called()

    def test_canonical_param(self):
        # It returns the court canonical_param
        court = mock_with_properties({"canonical_param": "court_canonical_param"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.canonical_param, "court_canonical_param")
        court.mock_canonical_param.assert_called()

    def test_param_aliases(self):
        # It returns the court param_aliases
        court = mock_with_properties({"param_aliases": "court_param_aliases"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.param_aliases, "court_param_aliases")
        court.mock_param_aliases.assert_called()

    def test_start_year(self):
        # It returns the court start_year
        court = mock_with_properties({"start_year": "court_start_year"})
        jurisdiction = mock_with_properties()
        cwj = CourtWithJurisdiction(court, jurisdiction)
        self.assertEqual(cwj.start_year, "court_start_year")
        court.mock_start_year.assert_called()

    def test_end_year(self):
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
