---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dynamic-modules
  - api/operation/list
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/atlassian-connect/1/app/module/dynamic"
category: "Dynamic modules"
writes_data: false
---
# Jira v3 - Get modules

**Get modules** — `GET /rest/atlassian-connect/1/app/module/dynamic`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get modules"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/atlassian-connect/1/app/module/dynamic
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all modules registered dynamically by the calling app.

**[Permissions](#permissions) required:** Only Connect apps can make this request.
