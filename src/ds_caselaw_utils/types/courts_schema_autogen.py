# Automatically generated file from a JSON schema


from typing import List, TypedDict, Union
from typing_extensions import Required


class RawCourt(TypedDict, total=False):
    """ Raw Court. """

    code: Required[str]
    """
    pattern: ^[A-Za-z]{2,}(-[A-Za-z0-9]+)*$

    Required property
    """

    name: Required[str]
    """ Required property """

    grouped_name: str
    param: str
    """ pattern: ^[a-z]{2,}(?:/[a-z0-9]+)?$ """

    extra_params: List["_RawCourtExtraParamsItem"]
    ncn_pattern: str
    """
    Neutral Citation Pattern.

    A regular expression pattern which matches valid NCNs from this court.
    """

    link: Required[str]
    """
    format: uri

    Required property
    """

    start_year: int
    """ minimum: 1066 """

    end_year: int
    listable: Required[bool]
    """ Required property """

    selectable: Required[bool]
    """ Required property """

    jurisdictions: List["RawJurisdiction"]


class RawCourtGroup(TypedDict, total=False):
    """ Raw Court Group. """

    name: Required[str]
    """ Required property """

    display_name: Required[Union[str, None]]
    """ Required property """

    is_tribunal: Required[bool]
    """ Required property """

    courts: Required[List["RawCourt"]]
    """ Required property """



RawCourtRepository = List["RawCourtGroup"]
"""
Raw Court List.

A list of courts
"""



class RawJurisdiction(TypedDict, total=False):
    """ Raw Jurisdiction. """

    prefix: Required[str]
    """ Required property """

    name: Required[str]
    """ Required property """

    code: Required[str]
    """ Required property """



_RawCourtExtraParamsItem = str
""" pattern: ^[a-z]{2,}(/[a-z]+)?$ """

