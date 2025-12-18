# Parser metadata

- [1. Property `Parser metadata > documentType`](#documentType)
- [2. Property `Parser metadata > uri`](#uri)
- [3. Property `Parser metadata > court`](#court)
- [4. Property `Parser metadata > cite`](#cite)
- [5. Property `Parser metadata > date`](#date)
  - [5.1. Property `Parser metadata > date > oneOf > Date not provided`](#date_oneOf_i0)
  - [5.2. Property `Parser metadata > date > oneOf > Date of document publication`](#date_oneOf_i1)
- [6. Property `Parser metadata > name`](#name)
- [7. Property `Parser metadata > attachments`](#attachments)
- [8. Property `Parser metadata > error-messages`](#error-messages)
- [9. Property `Parser metadata > extensions`](#extensions)

**Title:** Parser metadata

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                             | Pattern | Type             | Deprecated | Definition | Title/Description |
| ------------------------------------ | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [documentType](#documentType )     | No      | enum (of string) | No         | -          | Type of document  |
| - [uri](#uri )                       | No      | string           | No         | -          | -                 |
| - [court](#court )                   | No      | string           | No         | -          | -                 |
| - [cite](#cite )                     | No      | string or null   | No         | -          | -                 |
| - [date](#date )                     | No      | Combination      | No         | -          | -                 |
| - [name](#name )                     | No      | string           | No         | -          | Name of document  |
| - [attachments](#attachments )       | No      | array            | No         | -          | -                 |
| - [error-messages](#error-messages ) | No      | array            | No         | -          | -                 |
| - [extensions](#extensions )         | No      | null             | No         | -          | -                 |

## <a name="documentType"></a>1. Property `Parser metadata > documentType`

**Title:** Type of document

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Must be one of the document types supported by Find Case Law.

Must be one of:
* "judgment"
* "pressSummary"

## <a name="uri"></a>2. Property `Parser metadata > uri`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

## <a name="court"></a>3. Property `Parser metadata > court`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="cite"></a>4. Property `Parser metadata > cite`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

## <a name="date"></a>5. Property `Parser metadata > date`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                 |
| ---------------------------------------------- |
| [Date not provided](#date_oneOf_i0)            |
| [Date of document publication](#date_oneOf_i1) |

### <a name="date_oneOf_i0"></a>5.1. Property `Parser metadata > date > oneOf > Date not provided`

**Title:** Date not provided

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="date_oneOf_i1"></a>5.2. Property `Parser metadata > date > oneOf > Date of document publication`

**Title:** Date of document publication

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

## <a name="name"></a>6. Property `Parser metadata > name`

**Title:** Name of document

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="attachments"></a>7. Property `Parser metadata > attachments`

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

## <a name="error-messages"></a>8. Property `Parser metadata > error-messages`

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

## <a name="extensions"></a>9. Property `Parser metadata > extensions`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
