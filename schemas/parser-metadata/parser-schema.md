# Parser process metadata

- [1. Property `Parser process metadata > documentType`](#documentType)
- [2. Property `Parser process metadata > uri`](#uri)
- [3. Property `Parser process metadata > court`](#court)
- [4. Property `Parser process metadata > cite`](#cite)
- [5. Property `Parser process metadata > date`](#date)
  - [5.1. Property `Parser process metadata > date > oneOf > Null`](#date_oneOf_i0)
  - [5.2. Property `Parser process metadata > date > oneOf > Date`](#date_oneOf_i1)
- [6. Property `Parser process metadata > name`](#name)
- [7. Property `Parser process metadata > attachments`](#attachments)
  - [7.1. Property `Parser process metadata > attachments > oneOf > Null`](#attachments_oneOf_i0)
  - [7.2. Property `Parser process metadata > attachments > oneOf > Array of attachments`](#attachments_oneOf_i1)
    - [7.2.1. Parser process metadata > attachments > oneOf > Array of attachments > item 1 items](#attachments_oneOf_i1_items)
      - [7.2.1.1. Property `Parser process metadata > attachments > oneOf > Array of attachments > item 1 items > name`](#attachments_oneOf_i1_items_name)
      - [7.2.1.2. Property `Parser process metadata > attachments > oneOf > Array of attachments > item 1 items > link`](#attachments_oneOf_i1_items_link)
- [8. Property `Parser process metadata > error-messages`](#error-messages)
- [9. Property `Parser process metadata > extensions`](#extensions)

**Title:** Parser process metadata

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Metadata about a document or its processing which has been generated or collated as a result of the Find Case Law parsing process.

| Property                             | Pattern | Type             | Deprecated | Definition | Title/Description |
| ------------------------------------ | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [documentType](#documentType )     | No      | enum (of string) | No         | -          | Type of document  |
| - [uri](#uri )                       | No      | string or null   | No         | -          | Document URI      |
| - [court](#court )                   | No      | string           | No         | -          | Court             |
| - [cite](#cite )                     | No      | string or null   | No         | -          | Citation          |
| - [date](#date )                     | No      | Combination      | No         | -          | Date of document  |
| - [name](#name )                     | No      | string           | No         | -          | Name of document  |
| - [attachments](#attachments )       | No      | Combination      | No         | -          | Attachments       |
| - [error-messages](#error-messages ) | No      | array            | No         | -          | Error messages    |
| - [extensions](#extensions )         | No      | null or object   | No         | -          | -                 |

## <a name="documentType"></a>1. Property `Parser process metadata > documentType`

**Title:** Type of document

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "decision"
* "judgment"
* "pressSummary"

## <a name="uri"></a>2. Property `Parser process metadata > uri`

**Title:** Document URI

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |
| **Format**   | `uri`            |

## <a name="court"></a>3. Property `Parser process metadata > court`

**Title:** Court

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** An FCL court identifier code. Must be one of the values in the [list of courts](https://github.com/nationalarchives/ds-caselaw-utils/blob/main/courts.md).

## <a name="cite"></a>4. Property `Parser process metadata > cite`

**Title:** Citation

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

## <a name="date"></a>5. Property `Parser process metadata > date`

**Title:** Date of document

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The primary date of the document. Usually publication date, hand-down date, decision date or similar.

| One of(Option)         |
| ---------------------- |
| [Null](#date_oneOf_i0) |
| [Date](#date_oneOf_i1) |

### <a name="date_oneOf_i0"></a>5.1. Property `Parser process metadata > date > oneOf > Null`

**Title:** Null

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="date_oneOf_i1"></a>5.2. Property `Parser process metadata > date > oneOf > Date`

**Title:** Date

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

## <a name="name"></a>6. Property `Parser process metadata > name`

**Title:** Name of document

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The title of the document for indexing purposes. May be different from the exact text which appears in the document.

## <a name="attachments"></a>7. Property `Parser process metadata > attachments`

**Title:** Attachments

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of attachments to the document.

| One of(Option)                                |
| --------------------------------------------- |
| [Null](#attachments_oneOf_i0)                 |
| [Array of attachments](#attachments_oneOf_i1) |

### <a name="attachments_oneOf_i0"></a>7.1. Property `Parser process metadata > attachments > oneOf > Null`

**Title:** Null

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="attachments_oneOf_i1"></a>7.2. Property `Parser process metadata > attachments > oneOf > Array of attachments`

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

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [item 1 items](#attachments_oneOf_i1_items) | -           |

#### <a name="attachments_oneOf_i1_items"></a>7.2.1. Parser process metadata > attachments > oneOf > Array of attachments > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                    | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [name](#attachments_oneOf_i1_items_name ) | No      | string | No         | -          | -                 |
| + [link](#attachments_oneOf_i1_items_link ) | No      | string | No         | -          | -                 |

##### <a name="attachments_oneOf_i1_items_name"></a>7.2.1.1. Property `Parser process metadata > attachments > oneOf > Array of attachments > item 1 items > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="attachments_oneOf_i1_items_link"></a>7.2.1.2. Property `Parser process metadata > attachments > oneOf > Array of attachments > item 1 items > link`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="error-messages"></a>8. Property `Parser process metadata > error-messages`

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

## <a name="extensions"></a>9. Property `Parser process metadata > extensions`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
