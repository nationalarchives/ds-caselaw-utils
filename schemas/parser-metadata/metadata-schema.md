# Parsed document metadata

- [1. Property `Parsed document metadata > parameters`](#parameters)
  - [1.1. Property `Parsed document metadata > parameters > PARSER`](#parameters_PARSER)
    - [1.1.1. Property `Parsed document metadata > parameters > PARSER > documentType`](#parameters_PARSER_documentType)
    - [1.1.2. Property `Parsed document metadata > parameters > PARSER > uri`](#parameters_PARSER_uri)
    - [1.1.3. Property `Parsed document metadata > parameters > PARSER > court`](#parameters_PARSER_court)
    - [1.1.4. Property `Parsed document metadata > parameters > PARSER > cite`](#parameters_PARSER_cite)
    - [1.1.5. Property `Parsed document metadata > parameters > PARSER > date`](#parameters_PARSER_date)
      - [1.1.5.1. Property `Parsed document metadata > parameters > PARSER > date > oneOf > Null`](#parameters_PARSER_date_oneOf_i0)
      - [1.1.5.2. Property `Parsed document metadata > parameters > PARSER > date > oneOf > Date`](#parameters_PARSER_date_oneOf_i1)
    - [1.1.6. Property `Parsed document metadata > parameters > PARSER > name`](#parameters_PARSER_name)
    - [1.1.7. Property `Parsed document metadata > parameters > PARSER > attachments`](#parameters_PARSER_attachments)
      - [1.1.7.1. Property `Parsed document metadata > parameters > PARSER > attachments > oneOf > Null`](#parameters_PARSER_attachments_oneOf_i0)
      - [1.1.7.2. Property `Parsed document metadata > parameters > PARSER > attachments > oneOf > Array of attachments`](#parameters_PARSER_attachments_oneOf_i1)
        - [1.1.7.2.1. Parsed document metadata > parameters > PARSER > attachments > oneOf > Array of attachments > item 1 items](#parameters_PARSER_attachments_oneOf_i1_items)
          - [1.1.7.2.1.1. Property `Parsed document metadata > parameters > PARSER > attachments > oneOf > Array of attachments > item 1 items > name`](#parameters_PARSER_attachments_oneOf_i1_items_name)
          - [1.1.7.2.1.2. Property `Parsed document metadata > parameters > PARSER > attachments > oneOf > Array of attachments > item 1 items > link`](#parameters_PARSER_attachments_oneOf_i1_items_link)
    - [1.1.8. Property `Parsed document metadata > parameters > PARSER > error-messages`](#parameters_PARSER_error-messages)
    - [1.1.9. Property `Parsed document metadata > parameters > PARSER > extensions`](#parameters_PARSER_extensions)
    - [1.1.10. Property `Parsed document metadata > parameters > PARSER > jurisdictionShortNames`](#parameters_PARSER_jurisdictionShortNames)
    - [1.1.11. Property `Parsed document metadata > parameters > PARSER > primary_source`](#parameters_PARSER_primary_source)
      - [1.1.11.1. Property `Parsed document metadata > parameters > PARSER > primary_source > filename`](#parameters_PARSER_primary_source_filename)
      - [1.1.11.2. Property `Parsed document metadata > parameters > PARSER > primary_source > sha256`](#parameters_PARSER_primary_source_sha256)
      - [1.1.11.3. Property `Parsed document metadata > parameters > PARSER > primary_source > mimetype`](#parameters_PARSER_primary_source_mimetype)
      - [1.1.11.4. Property `Parsed document metadata > parameters > PARSER > primary_source > route`](#parameters_PARSER_primary_source_route)
    - [1.1.12. Property `Parsed document metadata > parameters > PARSER > metadata_fields`](#parameters_PARSER_metadata_fields)
      - [1.1.12.1. Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items](#parameters_PARSER_metadata_fields_items)
        - [1.1.12.1.1. Property `Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items > id`](#parameters_PARSER_metadata_fields_items_id)
        - [1.1.12.1.2. Property `Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items > name`](#parameters_PARSER_metadata_fields_items_name)
        - [1.1.12.1.3. Property `Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items > value`](#parameters_PARSER_metadata_fields_items_value)
        - [1.1.12.1.4. Property `Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items > source`](#parameters_PARSER_metadata_fields_items_source)
        - [1.1.12.1.5. Property `Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items > timestamp`](#parameters_PARSER_metadata_fields_items_timestamp)
    - [1.1.13. Property `Parsed document metadata > parameters > PARSER > xml_contains_document_text`](#parameters_PARSER_xml_contains_document_text)
  - [1.2. Property `Parsed document metadata > parameters > INGESTER_OPTIONS`](#parameters_INGESTER_OPTIONS)
    - [1.2.1. Property `Parsed document metadata > parameters > INGESTER_OPTIONS > auto_publish`](#parameters_INGESTER_OPTIONS_auto_publish)
    - [1.2.2. Property `Parsed document metadata > parameters > INGESTER_OPTIONS > source_document`](#parameters_INGESTER_OPTIONS_source_document)
      - [1.2.2.1. Property `Parsed document metadata > parameters > INGESTER_OPTIONS > source_document > format`](#parameters_INGESTER_OPTIONS_source_document_format)
      - [1.2.2.2. Property `Parsed document metadata > parameters > INGESTER_OPTIONS > source_document > file_hash`](#parameters_INGESTER_OPTIONS_source_document_file_hash)
  - [1.3. Property `Parsed document metadata > parameters > TDR`](#parameters_TDR)
  - [1.4. Property `Parsed document metadata > parameters > TRE`](#parameters_TRE)

**Title:** Parsed document metadata

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [parameters](#parameters ) | No      | object | No         | -          | -                 |

## <a name="parameters"></a>1. Property `Parsed document metadata > parameters`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| Property                                            | Pattern | Type   | Deprecated | Definition                       | Title/Description        |
| --------------------------------------------------- | ------- | ------ | ---------- | -------------------------------- | ------------------------ |
| + [PARSER](#parameters_PARSER )                     | No      | object | No         | In parser.schema.json#           | Parser process metadata  |
| - [INGESTER_OPTIONS](#parameters_INGESTER_OPTIONS ) | No      | object | No         | In ingester_options.schema.json# | Parsed document metadata |
| - [TDR](#parameters_TDR )                           | No      | object | No         | -                                | TDR process metadata     |
| - [TRE](#parameters_TRE )                           | No      | object | No         | -                                | TRE process metadata     |

### <a name="parameters_PARSER"></a>1.1. Property `Parsed document metadata > parameters > PARSER`

**Title:** Parser process metadata

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Required**              | Yes                 |
| **Additional properties** | Not allowed         |
| **Defined in**            | parser.schema.json# |

**Description:** Metadata about a document or its processing which has been generated or collated as a result of the Find Case Law parsing process.

| Property                                                                       | Pattern | Type             | Deprecated | Definition | Title/Description                                                                                                                                                             |
| ------------------------------------------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| + [documentType](#parameters_PARSER_documentType )                             | No      | enum (of string) | No         | -          | Type of document                                                                                                                                                              |
| - [uri](#parameters_PARSER_uri )                                               | No      | string or null   | No         | -          | Document URI                                                                                                                                                                  |
| - [court](#parameters_PARSER_court )                                           | No      | string           | No         | -          | Court                                                                                                                                                                         |
| - [cite](#parameters_PARSER_cite )                                             | No      | string or null   | No         | -          | Citation                                                                                                                                                                      |
| - [date](#parameters_PARSER_date )                                             | No      | Combination      | No         | -          | Date of document                                                                                                                                                              |
| - [name](#parameters_PARSER_name )                                             | No      | string           | No         | -          | Name of document                                                                                                                                                              |
| - [attachments](#parameters_PARSER_attachments )                               | No      | Combination      | No         | -          | Attachments                                                                                                                                                                   |
| - [error-messages](#parameters_PARSER_error-messages )                         | No      | array            | No         | -          | Error messages                                                                                                                                                                |
| - [extensions](#parameters_PARSER_extensions )                                 | No      | null or object   | No         | -          | -                                                                                                                                                                             |
| - [jurisdictionShortNames](#parameters_PARSER_jurisdictionShortNames )         | No      | array            | No         | -          | -                                                                                                                                                                             |
| - [primary_source](#parameters_PARSER_primary_source )                         | No      | object           | No         | -          | Primary source file                                                                                                                                                           |
| - [metadata_fields](#parameters_PARSER_metadata_fields )                       | No      | array of object  | No         | -          | Metadata fields                                                                                                                                                               |
| - [xml_contains_document_text](#parameters_PARSER_xml_contains_document_text ) | No      | boolean          | No         | -          | An indicator of if the XML of the document contains body text which is renderable for human consumption, instead of only being a stub containing metadata for a static asset. |

#### <a name="parameters_PARSER_documentType"></a>1.1.1. Property `Parsed document metadata > parameters > PARSER > documentType`

**Title:** Type of document

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "decision"
* "judgment"
* "pressSummary"

#### <a name="parameters_PARSER_uri"></a>1.1.2. Property `Parsed document metadata > parameters > PARSER > uri`

**Title:** Document URI

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |
| **Format**   | `uri`            |

#### <a name="parameters_PARSER_court"></a>1.1.3. Property `Parsed document metadata > parameters > PARSER > court`

**Title:** Court

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** An FCL court identifier code. Must be one of the values in the [list of courts](https://github.com/nationalarchives/ds-caselaw-utils/blob/main/courts.md).

#### <a name="parameters_PARSER_cite"></a>1.1.4. Property `Parsed document metadata > parameters > PARSER > cite`

**Title:** Citation

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

#### <a name="parameters_PARSER_date"></a>1.1.5. Property `Parsed document metadata > parameters > PARSER > date`

**Title:** Date of document

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The primary date of the document. Usually publication date, hand-down date, decision date or similar.

| One of(Option)                           |
| ---------------------------------------- |
| [Null](#parameters_PARSER_date_oneOf_i0) |
| [Date](#parameters_PARSER_date_oneOf_i1) |

##### <a name="parameters_PARSER_date_oneOf_i0"></a>1.1.5.1. Property `Parsed document metadata > parameters > PARSER > date > oneOf > Null`

**Title:** Null

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="parameters_PARSER_date_oneOf_i1"></a>1.1.5.2. Property `Parsed document metadata > parameters > PARSER > date > oneOf > Date`

**Title:** Date

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

#### <a name="parameters_PARSER_name"></a>1.1.6. Property `Parsed document metadata > parameters > PARSER > name`

**Title:** Name of document

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The title of the document for indexing purposes. May be different from the exact text which appears in the document.

#### <a name="parameters_PARSER_attachments"></a>1.1.7. Property `Parsed document metadata > parameters > PARSER > attachments`

**Title:** Attachments

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of attachments to the document.

| One of(Option)                                                  |
| --------------------------------------------------------------- |
| [Null](#parameters_PARSER_attachments_oneOf_i0)                 |
| [Array of attachments](#parameters_PARSER_attachments_oneOf_i1) |

##### <a name="parameters_PARSER_attachments_oneOf_i0"></a>1.1.7.1. Property `Parsed document metadata > parameters > PARSER > attachments > oneOf > Null`

**Title:** Null

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="parameters_PARSER_attachments_oneOf_i1"></a>1.1.7.2. Property `Parsed document metadata > parameters > PARSER > attachments > oneOf > Array of attachments`

**Title:** Array of attachments

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                               | Description |
| ------------------------------------------------------------- | ----------- |
| [item 1 items](#parameters_PARSER_attachments_oneOf_i1_items) | -           |

###### <a name="parameters_PARSER_attachments_oneOf_i1_items"></a>1.1.7.2.1. Parsed document metadata > parameters > PARSER > attachments > oneOf > Array of attachments > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                      | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [name](#parameters_PARSER_attachments_oneOf_i1_items_name ) | No      | string | No         | -          | -                 |
| + [link](#parameters_PARSER_attachments_oneOf_i1_items_link ) | No      | string | No         | -          | -                 |

###### <a name="parameters_PARSER_attachments_oneOf_i1_items_name"></a>1.1.7.2.1.1. Property `Parsed document metadata > parameters > PARSER > attachments > oneOf > Array of attachments > item 1 items > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

###### <a name="parameters_PARSER_attachments_oneOf_i1_items_link"></a>1.1.7.2.1.2. Property `Parsed document metadata > parameters > PARSER > attachments > oneOf > Array of attachments > item 1 items > link`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

#### <a name="parameters_PARSER_error-messages"></a>1.1.8. Property `Parsed document metadata > parameters > PARSER > error-messages`

**Title:** Error messages

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A list of error messages raised whilst parsing this document.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

#### <a name="parameters_PARSER_extensions"></a>1.1.9. Property `Parsed document metadata > parameters > PARSER > extensions`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

#### <a name="parameters_PARSER_jurisdictionShortNames"></a>1.1.10. Property `Parsed document metadata > parameters > PARSER > jurisdictionShortNames`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

#### <a name="parameters_PARSER_primary_source"></a>1.1.11. Property `Parsed document metadata > parameters > PARSER > primary_source`

**Title:** Primary source file

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about the primary source file which was parsed.

| Property                                                  | Pattern | Type             | Deprecated | Definition | Title/Description                                  |
| --------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | -------------------------------------------------- |
| + [filename](#parameters_PARSER_primary_source_filename ) | No      | string           | No         | -          | The name of the file which was parsed.             |
| + [sha256](#parameters_PARSER_primary_source_sha256 )     | No      | string           | No         | -          | The SHA256 hash of the file.                       |
| + [mimetype](#parameters_PARSER_primary_source_mimetype ) | No      | string           | No         | -          | The MIME type of the file.                         |
| + [route](#parameters_PARSER_primary_source_route )       | No      | enum (of string) | No         | -          | The route which the file took to reach the parser. |

##### <a name="parameters_PARSER_primary_source_filename"></a>1.1.11.1. Property `Parsed document metadata > parameters > PARSER > primary_source > filename`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the file which was parsed.

##### <a name="parameters_PARSER_primary_source_sha256"></a>1.1.11.2. Property `Parsed document metadata > parameters > PARSER > primary_source > sha256`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The SHA256 hash of the file.

| Restrictions                      |                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[A-Fa-f0-9]{64}$``` [Test](https://regex101.com/?regex=%5E%5BA-Fa-f0-9%5D%7B64%7D%24) |

##### <a name="parameters_PARSER_primary_source_mimetype"></a>1.1.11.3. Property `Parsed document metadata > parameters > PARSER > primary_source > mimetype`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The MIME type of the file.

##### <a name="parameters_PARSER_primary_source_route"></a>1.1.11.4. Property `Parsed document metadata > parameters > PARSER > primary_source > route`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** The route which the file took to reach the parser.

Must be one of:
* "TDR"
* "BULK"
* "EUI"

#### <a name="parameters_PARSER_metadata_fields"></a>1.1.12. Property `Parsed document metadata > parameters > PARSER > metadata_fields`

**Title:** Metadata fields

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

**Description:** A list of additional metadata fields, either extracted from the document or sourced from a supplementary file.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                   | Description |
| ----------------------------------------------------------------- | ----------- |
| [metadata_fields items](#parameters_PARSER_metadata_fields_items) | -           |

##### <a name="parameters_PARSER_metadata_fields_items"></a>1.1.12.1. Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                           | Pattern | Type             | Deprecated | Definition | Title/Description              |
| ------------------------------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ------------------------------ |
| - [id](#parameters_PARSER_metadata_fields_items_id )               | No      | string           | No         | -          | Identifier                     |
| + [name](#parameters_PARSER_metadata_fields_items_name )           | No      | string           | No         | -          | Metadata name                  |
| + [value](#parameters_PARSER_metadata_fields_items_value )         | No      | string or object | No         | -          | Metadata value                 |
| + [source](#parameters_PARSER_metadata_fields_items_source )       | No      | enum (of string) | No         | -          | Metadata source                |
| + [timestamp](#parameters_PARSER_metadata_fields_items_timestamp ) | No      | string           | No         | -          | Timestamp of metadata creation |

###### <a name="parameters_PARSER_metadata_fields_items_id"></a>1.1.12.1.1. Property `Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items > id`

**Title:** Identifier

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="parameters_PARSER_metadata_fields_items_name"></a>1.1.12.1.2. Property `Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items > name`

**Title:** Metadata name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of this piece of metadata

| Restrictions                      |                                                                         |
| --------------------------------- | ----------------------------------------------------------------------- |
| **Must match regular expression** | ```^[a-z_]+$``` [Test](https://regex101.com/?regex=%5E%5Ba-z_%5D%2B%24) |

###### <a name="parameters_PARSER_metadata_fields_items_value"></a>1.1.12.1.3. Property `Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items > value`

**Title:** Metadata value

|              |                    |
| ------------ | ------------------ |
| **Type**     | `string or object` |
| **Required** | Yes                |

**Description:** A value for this metadata. May be either a plain string, or a JSON object with additional complexity.

###### <a name="parameters_PARSER_metadata_fields_items_source"></a>1.1.12.1.4. Property `Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items > source`

**Title:** Metadata source

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** The origin of this piece of metadata.

Must be one of:
* "document"
* "external"
* "editor"

###### <a name="parameters_PARSER_metadata_fields_items_timestamp"></a>1.1.12.1.5. Property `Parsed document metadata > parameters > PARSER > metadata_fields > metadata_fields items > timestamp`

**Title:** Timestamp of metadata creation

|              |            |
| ------------ | ---------- |
| **Type**     | `string`   |
| **Required** | Yes        |
| **Format**   | `datetime` |

**Description:** The timestamp this piece of metadata was first detected or added.

#### <a name="parameters_PARSER_xml_contains_document_text"></a>1.1.13. Property `Parsed document metadata > parameters > PARSER > xml_contains_document_text`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** An indicator of if the XML of the document contains body text which is renderable for human consumption, instead of only being a stub containing metadata for a static asset.

### <a name="parameters_INGESTER_OPTIONS"></a>1.2. Property `Parsed document metadata > parameters > INGESTER_OPTIONS`

**Title:** Parsed document metadata

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | ingester_options.schema.json# |

| Property                                                           | Pattern | Type    | Deprecated | Definition | Title/Description                                   |
| ------------------------------------------------------------------ | ------- | ------- | ---------- | ---------- | --------------------------------------------------- |
| - [auto_publish](#parameters_INGESTER_OPTIONS_auto_publish )       | No      | boolean | No         | -          | Auto-publish document                               |
| - [source_document](#parameters_INGESTER_OPTIONS_source_document ) | No      | object  | No         | -          | Information about the source file which was parsed. |

#### <a name="parameters_INGESTER_OPTIONS_auto_publish"></a>1.2.1. Property `Parsed document metadata > parameters > INGESTER_OPTIONS > auto_publish`

**Title:** Auto-publish document

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** Should the ingester bypass the editorial approval process and automatically publish this document?

#### <a name="parameters_INGESTER_OPTIONS_source_document"></a>1.2.2. Property `Parsed document metadata > parameters > INGESTER_OPTIONS > source_document`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about the source file which was parsed.

| Property                                                               | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [format](#parameters_INGESTER_OPTIONS_source_document_format )       | No      | string | No         | -          | Docuent format    |
| + [file_hash](#parameters_INGESTER_OPTIONS_source_document_file_hash ) | No      | string | No         | -          | File hash         |

##### <a name="parameters_INGESTER_OPTIONS_source_document_format"></a>1.2.2.1. Property `Parsed document metadata > parameters > INGESTER_OPTIONS > source_document > format`

**Title:** Docuent format

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The MIME type of the source file.

##### <a name="parameters_INGESTER_OPTIONS_source_document_file_hash"></a>1.2.2.2. Property `Parsed document metadata > parameters > INGESTER_OPTIONS > source_document > file_hash`

**Title:** File hash

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The SHA256 hash of the source file.

| Restrictions                      |                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[A-Fa-f0-9]{64}$``` [Test](https://regex101.com/?regex=%5E%5BA-Fa-f0-9%5D%7B64%7D%24) |

### <a name="parameters_TDR"></a>1.3. Property `Parsed document metadata > parameters > TDR`

**Title:** TDR process metadata

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Metadata about a document or its processing which has been added as part of the TDR upload process.

### <a name="parameters_TRE"></a>1.4. Property `Parsed document metadata > parameters > TRE`

**Title:** TRE process metadata

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Metadata about a document or its processing which has been added as part of the TRE workflow.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
