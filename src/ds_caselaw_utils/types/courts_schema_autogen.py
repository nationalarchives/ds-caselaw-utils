from typing import Literal, Required, TypedDict


CourtCode = str
r"""
Court Code.

pattern: ^[A-Za-z]{2,}(-[A-Za-z0-9]+)*$
"""



class CourtRelationship(TypedDict, total=False):
    r"""
    Court relationship.

    An object describing the relationship between two courts.
    """

    court_code: Required["CourtCode"]
    r"""
    Court Code.

    pattern: ^[A-Za-z]{2,}(-[A-Za-z0-9]+)*$

    Required property
    """

    relationship_type: "_CourtRelationshipRelationshipType"


NeutralCitationNumber = str
r"""
Neutral Citation Number.

An example Neutral Citation Number, matching our expected generic NCN pattern.

pattern: ^\[([0-9]{4})\] ([a-zA-Z]+)(?: ([a-zA-Z]+))? ([0-9]+)(?: \(([a-zA-Z0-9]+)\))?$
"""



class RawCourt(TypedDict, total=False):
    r"""
    Raw Court.

    dependentRequired:
      end_year:
      - start_year
      ncn_examples:
      - ncn_pattern
      ncn_pattern:
      - ncn_examples
    allOf:
      - if:
          properties:
            selectable:
              const: true
        then:
          required:
          - param
      - if:
          properties:
            listable:
              const: true
        then:
          required:
          - param
    """

    code: Required["CourtCode"]
    r"""
    Court Code.

    pattern: ^[A-Za-z]{2,}(-[A-Za-z0-9]+)*$

    Required property
    """

    name: Required[str]
    r"""
    Name.

    The name of this court as it will commonly appear on Find Case Law.

    Required property
    """

    long_name: str
    r"""
    Long Name.

    Optionally, the formal name of this court where it differs from the `name`.
    """

    grouped_name: str
    param: str
    r"""
    Search parameter.

    The primary value for the `court` parameter to use when searching for this court.

    pattern: ^[a-z]{2,}(?:/[a-z0-9]+)?$
    """

    extra_params: list["_ExtraParametersItem"]
    r"""
    Extra parameters.

    A list of additional parameters which, if they appear as a `court` parameter in search, will be mapped to this court.
    """

    ncn_pattern: str
    r"""
    Neutral Citation Pattern.

    A regular expression pattern which matches valid NCNs from this court.
    """

    ncn_examples: list["NeutralCitationNumber"]
    r"""
    Neutral Citation examples.

    An array of example NCNs for this court.
    """

    link: Required[str]
    r"""
    format: uri

    Required property
    """

    identifier_iri: str
    r""" format: uri """

    start_year: int
    r"""
    Start year.

    The default start year of the document holding range for this court in Find Case Law.

    minimum: 1066
    """

    end_year: int
    r"""
    End year.

    If this court no longer publishes documents, the default end year of the document holding range for this court in Find Case Law.
    """

    listable: Required[bool]
    r"""
    Listable.

    Should this court appear in public lists of courts supported by Find Case Law?

    Required property
    """

    selectable: Required[bool]
    r"""
    Selectable.

    Should this court appear as a selectable option in the list of searchable courts?

    Required property
    """

    jurisdictions: list["RawJurisdiction"]
    relationships: list["CourtRelationship"]
    r"""
    Relationships.

    Other courts which this court relates to.
    """



class RawCourtGroup(TypedDict, total=False):
    r""" Raw Court Group. """

    name: Required[str]
    r""" Required property """

    display_name: Required[str | None]
    r""" Required property """

    is_tribunal: Required[bool]
    r""" Required property """

    courts: Required[list["RawCourt"]]
    r""" Required property """



RawCourtRepository = list["RawCourtGroup"]
r"""
Raw Court Repository.

A list of courts
"""



class RawJurisdiction(TypedDict, total=False):
    r""" Raw Jurisdiction. """

    prefix: Required[str]
    r""" Required property """

    name: Required[str]
    r""" Required property """

    code: Required[str]
    r""" Required property """



_CourtRelationshipRelationshipType = Literal['hears_appeals_from'] | Literal['hears_similar_cases_to'] | Literal['might_be_looking_for']
_COURTRELATIONSHIPRELATIONSHIPTYPE_HEARS_APPEALS_FROM: Literal['hears_appeals_from'] = "hears_appeals_from"
r"""The values for the '_CourtRelationshipRelationshipType' enum"""
_COURTRELATIONSHIPRELATIONSHIPTYPE_HEARS_SIMILAR_CASES_TO: Literal['hears_similar_cases_to'] = "hears_similar_cases_to"
r"""The values for the '_CourtRelationshipRelationshipType' enum"""
_COURTRELATIONSHIPRELATIONSHIPTYPE_MIGHT_BE_LOOKING_FOR: Literal['might_be_looking_for'] = "might_be_looking_for"
r"""The values for the '_CourtRelationshipRelationshipType' enum"""



_ExtraParametersItem = str
r""" pattern: ^[a-z]{2,}(/[a-z]+)?$ """

