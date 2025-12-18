# Metadata

- [1. Property `Metadata > parameters`](#parameters)
  - [1.1. Property `Metadata > parameters > PARSER`](#parameters_PARSER)
    - [1.1.1. Property `Metadata > parameters > PARSER > documentType`](#parameters_PARSER_documentType)
    - [1.1.2. Property `Metadata > parameters > PARSER > uri`](#parameters_PARSER_uri)
    - [1.1.3. Property `Metadata > parameters > PARSER > court`](#parameters_PARSER_court)
    - [1.1.4. Property `Metadata > parameters > PARSER > cite`](#parameters_PARSER_cite)
    - [1.1.5. Property `Metadata > parameters > PARSER > date`](#parameters_PARSER_date)
      - [1.1.5.1. Property `Metadata > parameters > PARSER > date > oneOf > Date not provided`](#parameters_PARSER_date_oneOf_i0)
      - [1.1.5.2. Property `Metadata > parameters > PARSER > date > oneOf > Date of document publication`](#parameters_PARSER_date_oneOf_i1)
    - [1.1.6. Property `Metadata > parameters > PARSER > name`](#parameters_PARSER_name)
    - [1.1.7. Property `Metadata > parameters > PARSER > attachments`](#parameters_PARSER_attachments)
    - [1.1.8. Property `Metadata > parameters > PARSER > error-messages`](#parameters_PARSER_error-messages)
    - [1.1.9. Property `Metadata > parameters > PARSER > extensions`](#parameters_PARSER_extensions)
  - [1.2. Property `Metadata > parameters > TDR`](#parameters_TDR)
  - [1.3. Property `Metadata > parameters > TRE`](#parameters_TRE)

**Title:** Metadata

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [parameters](#parameters ) | No      | object | No         | -          | -                 |

## <a name="parameters"></a>1. Property `Metadata > parameters`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | Yes         |
| **Additional properties** | Not allowed |

| Property                        | Pattern | Type   | Deprecated | Definition             | Title/Description |
| ------------------------------- | ------- | ------ | ---------- | ---------------------- | ----------------- |
| + [PARSER](#parameters_PARSER ) | No      | object | No         | In parser.schema.json# | Parser metadata   |
| - [TDR](#parameters_TDR )       | No      | object | No         | -                      | -                 |
| + [TRE](#parameters_TRE )       | No      | object | No         | -                      | -                 |

### <a name="parameters_PARSER"></a>1.1. Property `Metadata > parameters > PARSER`

**Title:** Parser metadata

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Required**              | Yes                 |
| **Additional properties** | Not allowed         |
| **Defined in**            | parser.schema.json# |

| Property                                               | Pattern | Type             | Deprecated | Definition | Title/Description |
| ------------------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [documentType](#parameters_PARSER_documentType )     | No      | enum (of string) | No         | -          | Type of document  |
| - [uri](#parameters_PARSER_uri )                       | No      | string           | No         | -          | -                 |
| - [court](#parameters_PARSER_court )                   | No      | string           | No         | -          | -                 |
| - [cite](#parameters_PARSER_cite )                     | No      | string or null   | No         | -          | -                 |
| - [date](#parameters_PARSER_date )                     | No      | Combination      | No         | -          | -                 |
| - [name](#parameters_PARSER_name )                     | No      | string           | No         | -          | Name of document  |
| - [attachments](#parameters_PARSER_attachments )       | No      | array            | No         | -          | -                 |
| - [error-messages](#parameters_PARSER_error-messages ) | No      | array            | No         | -          | -                 |
| - [extensions](#parameters_PARSER_extensions )         | No      | null             | No         | -          | -                 |

#### <a name="parameters_PARSER_documentType"></a>1.1.1. Property `Metadata > parameters > PARSER > documentType`

**Title:** Type of document

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Must be one of the document types supported by Find Case Law.

Must be one of:
* "judgment"
* "pressSummary"

#### <a name="parameters_PARSER_uri"></a>1.1.2. Property `Metadata > parameters > PARSER > uri`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

#### <a name="parameters_PARSER_court"></a>1.1.3. Property `Metadata > parameters > PARSER > court`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="parameters_PARSER_cite"></a>1.1.4. Property `Metadata > parameters > PARSER > cite`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

#### <a name="parameters_PARSER_date"></a>1.1.5. Property `Metadata > parameters > PARSER > date`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                   |
| ---------------------------------------------------------------- |
| [Date not provided](#parameters_PARSER_date_oneOf_i0)            |
| [Date of document publication](#parameters_PARSER_date_oneOf_i1) |

##### <a name="parameters_PARSER_date_oneOf_i0"></a>1.1.5.1. Property `Metadata > parameters > PARSER > date > oneOf > Date not provided`

**Title:** Date not provided

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="parameters_PARSER_date_oneOf_i1"></a>1.1.5.2. Property `Metadata > parameters > PARSER > date > oneOf > Date of document publication`

**Title:** Date of document publication

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

#### <a name="parameters_PARSER_name"></a>1.1.6. Property `Metadata > parameters > PARSER > name`

**Title:** Name of document

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="parameters_PARSER_attachments"></a>1.1.7. Property `Metadata > parameters > PARSER > attachments`

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

#### <a name="parameters_PARSER_error-messages"></a>1.1.8. Property `Metadata > parameters > PARSER > error-messages`

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

#### <a name="parameters_PARSER_extensions"></a>1.1.9. Property `Metadata > parameters > PARSER > extensions`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="parameters_TDR"></a>1.2. Property `Metadata > parameters > TDR`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

### <a name="parameters_TRE"></a>1.3. Property `Metadata > parameters > TRE`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
