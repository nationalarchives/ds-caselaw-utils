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



MetadataSource = Literal['document'] | Literal['external'] | Literal['editor']
r"""
Metadata source.

The origin of this piece of metadata.
"""
METADATASOURCE_DOCUMENT: Literal['document'] = "document"
r"""The values for the 'Metadata source' enum"""
METADATASOURCE_EXTERNAL: Literal['external'] = "external"
r"""The values for the 'Metadata source' enum"""
METADATASOURCE_EDITOR: Literal['editor'] = "editor"
r"""The values for the 'Metadata source' enum"""



MetadataValue = str | dict[str, Any]
r"""
Metadata value.

A value for this metadata. May be either a plain string, or a JSON object with additional complexity.
"""



Null: TypeAlias = None
r""" Null. """



Null0: TypeAlias = None
r""" Null. """



class ParsedDocumentMetadata(TypedDict, total=False):
    r""" Parsed document metadata. """

    auto_publish: bool
    r"""
    Auto-publish document.

    Should the ingester bypass the editorial approval process and automatically publish this document?
    """

    source_document: "_ParsedDocumentMetadataSourceDocument"
    r""" Information about the source file which was parsed. """



class ParsedDocumentMetadata0(TypedDict, total=False):
    r""" Parsed document metadata. """

    parameters: Required["_ParsedDocumentMetadataParameters"]
    r""" Required property """



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
    # | Primary source file.
    # | 
    # | Information about the primary source file which was parsed. This should usually be describing a document file such as a `.docx` or a `.pdf`, and not a container format such as `.zip`.
    'primary_source': "PrimarySourceFile",
    # | Metadata fields.
    # | 
    # | A list of additional metadata fields, either extracted from the document or sourced from a supplementary file.
    'metadata_fields': list["_MetadataFieldsItem"],
    # | An indicator of if the XML of the document contains body text which is renderable for human consumption, instead of only being a stub containing metadata for a static asset.
    # | 
    # | name: XML contains document text
    'xml_contains_document_text': bool,
}, total=False)


class PrimarySourceFile(TypedDict, total=False):
    r"""
    Primary source file.

    Information about the primary source file which was parsed. This should usually be describing a document file such as a `.docx` or a `.pdf`, and not a container format such as `.zip`.
    """

    filename: Required[str]
    r"""
    The filename (including extension) of the file which was parsed.

    name: Filename
    examples:
      - Foo v Bar [2026] UKSC 123.docx
      - Judgment v Judgement.pdf

    Required property
    """

    sha256: Required[str]
    r"""
    The SHA256 hash of the file.

    name: SHA256 hash
    pattern: ^[A-Fa-f0-9]{64}$

    Required property
    """

    mimetype: Required[str]
    r"""
    The MIME type of the file.

    name: MIME type
    examples:
      - application/vnd.openxmlformats-officedocument.wordprocessingml.document
      - application/pdf

    Required property
    """

    route: Required["_PrimarySourceFileRoute"]
    r"""
    The route which the file took to reach the parser.

    name: Route

    Required property
    """



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



class _MetadataFieldsItem(TypedDict, total=False):
    r"""
    allOf:
      - if:
          properties:
            name:
              const: title
        then:
          properties:
            value:
              type: string
      - if:
          properties:
            name:
              const: headnote
        then:
          properties:
            value:
              type: string
      - if:
          properties:
            name:
              const: category
        then:
          properties:
            value:
              properties:
                name:
                  title: Category name
                  type: string
                parent:
                  description: If this is a subcategory, the name of the parent category
                  title: Category parent
                  type:
                  - string
                  - 'null'
              required:
              - name
              - parent
              type: object
    """

    id: str
    r"""
    Identifier.

    A UUID for this piece of metadata.

    A new UUID should be generated only if the metadata value has changed; if there is an existing piece of metadata with the same source and same value the existing `id` should be used.

    format: uuid
    """

    name: Required[str]
    r"""
    Metadata name.

    The name of this piece of metadata

    pattern: ^[a-z_]+$

    Required property
    """

    value: Required["MetadataValue"]
    r"""
    Metadata value.

    A value for this metadata. May be either a plain string, or a JSON object with additional complexity.

    Required property
    """

    source: Required["MetadataSource"]
    r"""
    Metadata source.

    The origin of this piece of metadata.

    Required property
    """

    timestamp: Required[str]
    r"""
    Timestamp of metadata creation.

    The timestamp this piece of metadata was first detected or added.

    format: datetime

    Required property
    """



class _ParsedDocumentMetadataParameters(TypedDict, total=False):
    PARSER: Required["ParserProcessMetadata"]
    r"""
    Parser process metadata.

    Metadata about a document or its processing which has been generated or collated as a result of the Find Case Law parsing process.

    Required property
    """

    INGESTER_OPTIONS: "ParsedDocumentMetadata"
    r""" Parsed document metadata. """

    TDR: dict[str, Any]
    r"""
    TDR process metadata.

    Metadata about a document or its processing which has been added as part of the TDR upload process.
    """

    TRE: dict[str, Any]
    r"""
    TRE process metadata.

    Metadata about a document or its processing which has been added as part of the TRE workflow.
    """



class _ParsedDocumentMetadataSourceDocument(TypedDict, total=False):
    r""" Information about the source file which was parsed. """

    format: Required[str]
    r"""
    Docuent format.

    The MIME type of the source file.

    Required property
    """

    file_hash: Required[str]
    r"""
    File hash.

    The SHA256 hash of the source file.

    pattern: ^[A-Fa-f0-9]{64}$

    Required property
    """



_PrimarySourceFileRoute = Literal['TDR'] | Literal['BULK'] | Literal['EUI']
r"""
The route which the file took to reach the parser.

name: Route
"""
_PRIMARYSOURCEFILEROUTE_TDR: Literal['TDR'] = "TDR"
r"""The values for the 'The route which the file took to reach the parser' enum"""
_PRIMARYSOURCEFILEROUTE_BULK: Literal['BULK'] = "BULK"
r"""The values for the 'The route which the file took to reach the parser' enum"""
_PRIMARYSOURCEFILEROUTE_EUI: Literal['EUI'] = "EUI"
r"""The values for the 'The route which the file took to reach the parser' enum"""

