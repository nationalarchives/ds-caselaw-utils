from typing import Literal, Required, TypeAlias, TypedDict, Union


Citation = str | None
r""" Citation. """



Date = str
r"""
Date.

format: date
"""



Null: TypeAlias = None
r""" Null. """



# | Parser process metadata.
# | 
# | Metadata about a document or its processing which has been generated or collated as a result of the Find Case Law parsing process.
ParserProcessMetadata = TypedDict('ParserProcessMetadata', {
    # | Type of document.
    # | 
    # | Must be one of the document types supported by Find Case Law.
    # | 
    # | Required property
    'documentType': Required["TypeOfDocument"],
    # | Document URI.
    # | 
    # | format: uri
    'uri': str,
    # | Court.
    'court': str,
    # | Citation.
    'cite': "Citation",
    # | Date of publication.
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
    # | WARNING: we get an array without any items
    'attachments': None,
    # | WARNING: we get an array without any items
    'error-messages': None,
    'extensions': None,
}, total=False)


TypeOfDocument = Literal['judgment'] | Literal['pressSummary']
r"""
Type of document.

Must be one of the document types supported by Find Case Law.
"""
TYPEOFDOCUMENT_JUDGMENT: Literal['judgment'] = "judgment"
r"""The values for the 'Type of document' enum"""
TYPEOFDOCUMENT_PRESSSUMMARY: Literal['pressSummary'] = "pressSummary"
r"""The values for the 'Type of document' enum"""

