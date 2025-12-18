from typing import Literal, TypeAlias, TypedDict, Union


DateNotProvided: TypeAlias = None
r""" Date not provided. """



DateOfDocumentPublication = str
r"""
Date of document publication.

format: date
"""



# | Parser process metadata.
# | 
# | Metadata about a document or its processing which has been generated or collated as a result of the Find Case Law parsing process.
ParserProcessMetadata = TypedDict('ParserProcessMetadata', {
    # | Type of document.
    # | 
    # | Must be one of the document types supported by Find Case Law.
    'documentType': "TypeOfDocument",
    # | format: uri
    'uri': str,
    'court': str,
    'cite': str | None,
    # | Aggregation type: oneOf
    # | Subtype: "DateNotProvided", "DateOfDocumentPublication"
    'date': Union["DateNotProvided", "DateOfDocumentPublication"],
    # | Name of document.
    'name': str,
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

