---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/app-migration
  - api/operation/search
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/atlassian-connect/1/migration/workflow/rule/search"
category: "App migration"
writes_data: false
---
# Jira v3 - Get workflow transition rule configurations

**Get workflow transition rule configurations** — `POST /rest/atlassian-connect/1/migration/workflow/rule/search`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get workflow transition rule configurations"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/atlassian-connect/1/migration/workflow/rule/search
Authorization: {{service.auth_token}}
Accept: application/json
Atlassian-Transfer-Id: {{param:atlassian_transfer_id}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `atlassian_transfer_id` (header, string, required) — Value of the `Atlassian-Transfer-Id` header.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Returns configurations for workflow transition rules migrated from server to cloud and owned by the calling Connect app.
