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
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/audit"
category: "Audit"
writes_data: false
tool_note: "[[confluence_v1_get_audit_records]]"
---
# Confluence v1 - Get audit records

**Get audit records** — `GET /wiki/rest/api/audit`

- Run by the tool [[confluence_v1_get_audit_records]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/audit?startDate={{param:startDate}}&endDate={{param:endDate}}&searchString={{param:searchString}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startDate` (query, string, optional) — Filters the results to the records on or after the startDate. The startDate must be specified as epoch time in milliseconds.
- `endDate` (query, string, optional) — Filters the results to the records on or before the endDate. The endDate must be specified as epoch time in milliseconds.
- `searchString` (query, string, optional) — Filters the results to records that have string property values matching the searchString.
- `start` (query, string, optional) — The starting index of the returned records.
- `limit` (query, string, optional) — The maximum number of records to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns all records in the audit log, optionally for a certain date range.
This contains information about events like space exports, group membership
changes, app installations, etc. For more information, see
[Audit log](https://confluence.atlassian.com/confcloud/audit-log-802164269.html)
in the Confluence administrator's guide.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Confluence Administrator' global permission.
