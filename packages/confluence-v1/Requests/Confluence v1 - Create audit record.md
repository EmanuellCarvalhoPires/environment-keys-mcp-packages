---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/audit
  - api/operation/create
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/audit"
category: "Audit"
writes_data: true
tool_note: "[[confluence_v1_create_audit_record]]"
---
# Confluence v1 - Create audit record

**Create audit record** — `POST /wiki/rest/api/audit`

- Run by the tool [[confluence_v1_create_audit_record]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/audit
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a record in the audit log.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Confluence Administrator' global permission.
