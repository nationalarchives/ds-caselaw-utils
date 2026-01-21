from typing import Any, Literal, Required, TypeAlias, TypedDict, Union


ArrayOfAttachments = list["_ArrayOfAttachmentsItem"]
r""" Array of attachments. """



Citation = str | None
r""" Citation. """



Date = str
r"""
Date.

format: date
"""



DocumentUri = str | None
r"""
Document URI.

format: uri
"""



Null: TypeAlias = None
r""" Null. """



Null0: TypeAlias = None
r""" Null. """



# | Parser process metadata.
# | 
# | Metadata about a document or its processing which has been generated or collated as a result of the Find Case Law parsing process.
ParserProcessMetadata = TypedDict('ParserProcessMetadata', {
    # | Type of document.
    # | 
    # | Required property
    'documentType': Required["TypeOfDocument"],
    # | Document URI.
    # | 
    # | format: uri
    'uri': "DocumentUri",
    # | Court.
    # | 
    # | An FCL court identifier code. Must be one of the values in the [list of courts](https://github.com/nationalarchives/ds-caselaw-utils/blob/main/courts.md).
    'court': str,
    # | Citation.
    'cite': "Citation",
    # | Date of document.
    # | 
    # | The primary date of the document. Usually publication date, hand-down date, decision date or similar.
    # | 
    # | Aggregation type: oneOf
    # | Subtype: "Null", "Date"
    'date': Union["Null", "Date"],
    # | Name of document.
    # | 
    # | The title of the document for indexing purposes. May be different from the exact text which appears in the document.
    'name': str,
    # | Attachments.
    # | 
    # | A list of attachments to the document.
    # | 
    # | Aggregation type: oneOf
    # | Subtype: "Null0", "ArrayOfAttachments"
    'attachments': Union["Null0", "ArrayOfAttachments"],
    # | Error messages.
    # | 
    # | A list of error messages raised whilst parsing this document.
    # | 
    # | WARNING: we get an array without any items
    'error-messages': None,
    'extensions': None | dict[str, Any],
    # | WARNING: we get an array without any items
    'jurisdictionShortNames': None,
}, total=False)


TypeOfDocument = Literal['decision'] | Literal['judgment'] | Literal['pressSummary']
r""" Type of document. """
TYPEOFDOCUMENT_DECISION: Literal['decision'] = "decision"
r"""The values for the 'Type of document' enum"""
TYPEOFDOCUMENT_JUDGMENT: Literal['judgment'] = "judgment"
r"""The values for the 'Type of document' enum"""
TYPEOFDOCUMENT_PRESSSUMMARY: Literal['pressSummary'] = "pressSummary"
r"""The values for the 'Type of document' enum"""



class _ArrayOfAttachmentsItem(TypedDict, total=False):
    name: Required[str]
    r""" Required property """

    link: Required[str]
    r""" Required property """

