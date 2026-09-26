---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/audit
  - api/operation/list
  - api/effect/read
  - api/version/v1
  - api/permission/global-admin
  - api/format/binary
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/audit/export"
category: "Audit"
writes_data: false
---
# Confluence v1 - Export audit records

**Export audit records** — `GET /wiki/rest/api/audit/export`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Confluence v1 - Export audit records"`.
- **Format:** the response is binary (file/image); the plugin returns the body as text.
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/audit/export?startDate={{param:startDate}}&endDate={{param:endDate}}&searchString={{param:searchString}}&format={{param:format}}
Authorization: {{service.auth_token}}
Accept: application/zip
```

## Parameters

- `startDate` (query, string, optional) — Filters the exported results to the records on or after the startDate. The startDate must be specified as epoch time in milliseconds.
- `endDate` (query, string, optional) — Filters the exported results to the records on or before the endDate. The endDate must be specified as epoch time in milliseconds.
- `searchString` (query, string, optional) — Filters the exported results to records that have string property values matching the searchString.
- `format` (query, string, optional) — The format of the export file for the audit records.

## Original description

Exports audit records as a CSV file or ZIP file.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Confluence Administrator' global permission.
