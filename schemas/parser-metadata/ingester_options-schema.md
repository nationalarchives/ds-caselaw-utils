# Parsed document metadata

- [1. Property `Parsed document metadata > auto_publish`](#auto_publish)
- [2. Property `Parsed document metadata > source_document`](#source_document)
  - [2.1. Property `Parsed document metadata > source_document > format`](#source_document_format)
  - [2.2. Property `Parsed document metadata > source_document > file_hash`](#source_document_file_hash)

**Title:** Parsed document metadata

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                               | Pattern | Type    | Deprecated | Definition | Title/Description                                   |
| -------------------------------------- | ------- | ------- | ---------- | ---------- | --------------------------------------------------- |
| - [auto_publish](#auto_publish )       | No      | boolean | No         | -          | Auto-publish document                               |
| - [source_document](#source_document ) | No      | object  | No         | -          | Information about the source file which was parsed. |

## <a name="auto_publish"></a>1. Property `Parsed document metadata > auto_publish`

**Title:** Auto-publish document

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** Should the ingester bypass the editorial approval process and automatically publish this document?

## <a name="source_document"></a>2. Property `Parsed document metadata > source_document`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about the source file which was parsed.

| Property                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [format](#source_document_format )       | No      | string | No         | -          | Docuent format    |
| + [file_hash](#source_document_file_hash ) | No      | string | No         | -          | File hash         |

### <a name="source_document_format"></a>2.1. Property `Parsed document metadata > source_document > format`

**Title:** Docuent format

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The MIME type of the source file.

### <a name="source_document_file_hash"></a>2.2. Property `Parsed document metadata > source_document > file_hash`

**Title:** File hash

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The SHA256 hash of the source file.

| Restrictions                      |                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[A-Fa-f0-9]{64}$``` [Test](https://regex101.com/?regex=%5E%5BA-Fa-f0-9%5D%7B64%7D%24) |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
