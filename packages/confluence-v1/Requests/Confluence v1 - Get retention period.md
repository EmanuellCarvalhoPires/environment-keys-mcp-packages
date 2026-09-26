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
path: "/wiki/rest/api/audit/retention"
category: "Audit"
writes_data: false
tool_note: "[[confluence_v1_get_retention_period]]"
---
# Confluence v1 - Get retention period

**Get retention period** — `GET /wiki/rest/api/audit/retention`

- Run by the tool [[confluence_v1_get_retention_period]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/audit/retention
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the retention period for records in the audit log. The retention
period is how long an audit record is kept for, from creation date until
it is deleted.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Confluence Administrator' global permission.
