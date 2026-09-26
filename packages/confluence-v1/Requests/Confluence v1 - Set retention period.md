---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/audit
  - api/operation/update
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/audit/retention"
category: "Audit"
writes_data: true
tool_note: "[[confluence_v1_set_retention_period]]"
---
# Confluence v1 - Set retention period

**Set retention period** — `PUT /wiki/rest/api/audit/retention`

- Run by the tool [[confluence_v1_set_retention_period]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/audit/retention
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the retention period for records in the audit log. The retention period
can be set to a maximum of 1 year.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Confluence Administrator' global permission.
