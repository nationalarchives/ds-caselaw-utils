# Automatically generated file from a JSON schema


from typing import Required, TypedDict


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

    code: Required[str]
    r"""
    pattern: ^[A-Za-z]{2,}(-[A-Za-z0-9]+)*$

    Required property
    """

    name: Required[str]
    r""" Required property """

    long_name: str
    grouped_name: str
    param: str
    r""" pattern: ^[a-z]{2,}(?:/[a-z0-9]+)?$ """

    extra_params: list["_RawCourtExtraParamsItem"]
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
    r""" minimum: 1066 """

    end_year: int
    listable: Required[bool]
    r""" Required property """

    selectable: Required[bool]
    r""" Required property """

    jurisdictions: list["RawJurisdiction"]


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
Raw Court List.

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



_RawCourtExtraParamsItem = str
r""" pattern: ^[a-z]{2,}(/[a-z]+)?$ """

