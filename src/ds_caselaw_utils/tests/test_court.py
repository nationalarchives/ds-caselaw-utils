import unittest
from datetime import date
from unittest.mock import MagicMock, PropertyMock, patch

from ds_caselaw_utils.courts import (
    Court,
    CourtWithJurisdiction,
    InstitutionType,
    RelationshipType,
)
from ds_caselaw_utils.tests.factory import CourtFactory


def mock_with_properties(properties=None):
    if properties is None:
        properties = {}

    # Use a per-call subclass so class-level PropertyMock assignments do not leak across other MagicMock instances.
    mock_cls = type("MockWithProperties", (MagicMock,), {})
    mock = mock_cls(spec=dict)

    for property_name, value in properties.items():
        property_mock = PropertyMock(return_value=value)
        setattr(mock_cls, property_name, property_mock)
        setattr(mock, "mock_%s" % property_name, property_mock)
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

    def test_is_ended_default(self):
        court = CourtFactory({})
        assert not court.is_ended

    def test_is_ended_explicit(self):
        court = CourtFactory({"ended": True})
        assert court.is_ended

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

    def test_relationships_default_to_empty(self):
        court = CourtFactory({})
        self.assertEqual([], court.relationships)
        self.assertEqual([], court.hears_appeals_from)
        self.assertEqual([], court.hears_similar_cases_to)

    @patch("ds_caselaw_utils.courts.courts.get_by_code")
    def test_relationships_of_type_filters_by_relationship_type(self, mock_get_by_code):
        related_court = CourtFactory({"code": "EWHC", "name": "High Court"})
        mock_get_by_code.return_value = related_court

        court = CourtFactory(
            {
                "relationships": [
                    {"court_code": "EWHC", "relationship_type": "hears_appeals_from"},
                    {"court_code": "EWCA", "relationship_type": "hears_similar_cases_to"},
                ]
            }
        )

        relationships = court.relationships_of_type(RelationshipType.HEARS_APPEALS_FROM)

        self.assertEqual(1, len(relationships))
        self.assertEqual("EWHC", relationships[0].court.code)
        self.assertEqual(RelationshipType.HEARS_APPEALS_FROM, relationships[0].relationship_type)
        mock_get_by_code.assert_called_once_with("EWHC")

    @patch("ds_caselaw_utils.courts.Court.relationships_of_type")
    def test_hears_appeals_from_returns_related_courts(self, mock_relationships_of_type):
        related_court = CourtFactory({"code": "EWHC", "name": "High Court"})
        mock_relationship = MagicMock(court=related_court)
        mock_relationships_of_type.return_value = [mock_relationship]

        court = CourtFactory({})

        assert court.hears_appeals_from == [related_court]
        mock_relationships_of_type.assert_called_once_with(RelationshipType.HEARS_APPEALS_FROM)

    @patch("ds_caselaw_utils.courts.Court.relationships_of_type")
    def test_hears_similar_cases_to_returns_related_courts(self, mock_relationships_of_type):
        related_court = CourtFactory({"code": "EWCA", "name": "Court of Appeal"})
        mock_relationship = MagicMock(court=related_court)
        mock_relationships_of_type.return_value = [mock_relationship]

        court = CourtFactory({})

        assert court.hears_similar_cases_to == [related_court]
        mock_relationships_of_type.assert_called_once_with(RelationshipType.SIMILAR_CASES_TO)

    @patch("ds_caselaw_utils.courts.Court.relationships_of_type")
    def test_might_be_looking_for_returns_related_courts(self, mock_relationships_of_type):
        related_court = CourtFactory({"code": "EWCA", "name": "Court of Appeal"})
        mock_relationship = MagicMock(court=related_court)
        mock_relationships_of_type.return_value = [mock_relationship]

        court = CourtFactory({})

        assert court.might_be_looking_for == [related_court]
        mock_relationships_of_type.assert_called_once_with(RelationshipType.LOOKING_FOR)


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
