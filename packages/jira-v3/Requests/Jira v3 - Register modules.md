---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dynamic-modules
  - api/operation/action
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/atlassian-connect/1/app/module/dynamic"
category: "Dynamic modules"
writes_data: true
---
# Jira v3 - Register modules

**Register modules** — `POST /rest/atlassian-connect/1/app/module/dynamic`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Register modules"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/atlassian-connect/1/app/module/dynamic
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Registers a list of modules.

**[Permissions](#permissions) required:** Only Connect apps can make this request.
