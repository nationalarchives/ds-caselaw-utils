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
    - [1.1.8. Property `Parsed document metadata > parameters > PARSER > error-messages`](#parameters_PARSER_error-messages)
    - [1.1.9. Property `Parsed document metadata > parameters > PARSER > extensions`](#parameters_PARSER_extensions)
  - [1.2. Property `Parsed document metadata > parameters > TDR`](#parameters_TDR)
  - [1.3. Property `Parsed document metadata > parameters > TRE`](#parameters_TRE)

**Title:** Parsed document metadata

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [parameters](#parameters ) | No      | object | No         | -          | -                 |

## <a name="parameters"></a>1. Property `Parsed document metadata > parameters`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| Property                        | Pattern | Type   | Deprecated | Definition             | Title/Description       |
| ------------------------------- | ------- | ------ | ---------- | ---------------------- | ----------------------- |
| + [PARSER](#parameters_PARSER ) | No      | object | No         | In parser.schema.json# | Parser process metadata |
| - [TDR](#parameters_TDR )       | No      | object | No         | -                      | TDR process metadata    |
| - [TRE](#parameters_TRE )       | No      | object | No         | -                      | TRE process metadata    |

### <a name="parameters_PARSER"></a>1.1. Property `Parsed document metadata > parameters > PARSER`

**Title:** Parser process metadata

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Required**              | Yes                 |
| **Additional properties** | Not allowed         |
| **Defined in**            | parser.schema.json# |

**Description:** Metadata about a document or its processing which has been generated or collated as a result of the Find Case Law parsing process.

| Property                                               | Pattern | Type             | Deprecated | Definition | Title/Description   |
| ------------------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ------------------- |
| + [documentType](#parameters_PARSER_documentType )     | No      | enum (of string) | No         | -          | Type of document    |
| - [uri](#parameters_PARSER_uri )                       | No      | string           | No         | -          | Document URI        |
| - [court](#parameters_PARSER_court )                   | No      | string           | No         | -          | Court               |
| - [cite](#parameters_PARSER_cite )                     | No      | string or null   | No         | -          | Citation            |
| - [date](#parameters_PARSER_date )                     | No      | Combination      | No         | -          | Date of publication |
| - [name](#parameters_PARSER_name )                     | No      | string           | No         | -          | Name of document    |
| - [attachments](#parameters_PARSER_attachments )       | No      | array            | No         | -          | Attachments         |
| - [error-messages](#parameters_PARSER_error-messages ) | No      | array            | No         | -          | -                   |
| - [extensions](#parameters_PARSER_extensions )         | No      | null             | No         | -          | -                   |

#### <a name="parameters_PARSER_documentType"></a>1.1.1. Property `Parsed document metadata > parameters > PARSER > documentType`

**Title:** Type of document

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** Must be one of the document types supported by Find Case Law.

Must be one of:
* "judgment"
* "pressSummary"

#### <a name="parameters_PARSER_uri"></a>1.1.2. Property `Parsed document metadata > parameters > PARSER > uri`

**Title:** Document URI

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

#### <a name="parameters_PARSER_court"></a>1.1.3. Property `Parsed document metadata > parameters > PARSER > court`

**Title:** Court

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="parameters_PARSER_cite"></a>1.1.4. Property `Parsed document metadata > parameters > PARSER > cite`

**Title:** Citation

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

#### <a name="parameters_PARSER_date"></a>1.1.5. Property `Parsed document metadata > parameters > PARSER > date`

**Title:** Date of publication

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

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

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A list of attachments to the document.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

#### <a name="parameters_PARSER_error-messages"></a>1.1.8. Property `Parsed document metadata > parameters > PARSER > error-messages`

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

#### <a name="parameters_PARSER_extensions"></a>1.1.9. Property `Parsed document metadata > parameters > PARSER > extensions`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="parameters_TDR"></a>1.2. Property `Parsed document metadata > parameters > TDR`

**Title:** TDR process metadata

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Metadata about a document or its processing which has been added as part of the TDR upload process.

### <a name="parameters_TRE"></a>1.3. Property `Parsed document metadata > parameters > TRE`

**Title:** TRE process metadata

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Metadata about a document or its processing which has been added as part of the TRE workflow.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
