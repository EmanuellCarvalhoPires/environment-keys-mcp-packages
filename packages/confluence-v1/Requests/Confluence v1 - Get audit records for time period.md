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
path: "/wiki/rest/api/audit/since"
category: "Audit"
writes_data: false
tool_note: "[[confluence_v1_get_audit_records_for_time_period]]"
---
# Confluence v1 - Get audit records for time period

**Get audit records for time period** — `GET /wiki/rest/api/audit/since`

- Run by the tool [[confluence_v1_get_audit_records_for_time_period]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/audit/since?number={{param:number}}&units={{param:units}}&searchString={{param:searchString}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `number` (query, string, optional) — The number of units for the time period.
- `units` (query, string, optional) — The unit of time that the time period is measured in.
- `searchString` (query, string, optional) — Filters the results to records that have string property values matching the searchString.
- `start` (query, string, optional) — The starting index of the returned records.
- `limit` (query, string, optional) — The maximum number of records to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns records from the audit log, for a time period back from the current
date. For example, you can use this method to get the last 3 months of records.

This contains information about events like space exports, group membership
changes, app installations, etc. For more information, see
[Audit log](https://confluence.atlassian.com/confcloud/audit-log-802164269.html)
in the Confluence administrator's guide.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Confluence Administrator' global permission.
