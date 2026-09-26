---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/dynamic-modules
  - api/operation/list
  - api/effect/read
  - api/version/v1
  - api/restriction/app-connect
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/atlassian-connect/1/app/module/dynamic"
category: "Dynamic modules"
writes_data: false
---
# Confluence v1 - Get modules

**Get modules** — `GET /wiki/rest/atlassian-connect/1/app/module/dynamic`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Confluence v1 - Get modules"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/atlassian-connect/1/app/module/dynamic
Authorization: {{service.auth_token}}
Accept: */*
```

## Original description

Returns all modules registered dynamically by the calling app.

**[Permissions](#permissions) required:** Only Connect apps can make this request.
