---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/dynamic-modules
  - api/operation/action
  - api/effect/write
  - api/version/v1
  - api/restriction/app-connect
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/atlassian-connect/1/app/module/dynamic"
category: "Dynamic modules"
writes_data: true
---
# Confluence v1 - Register modules

**Register modules** — `POST /wiki/rest/atlassian-connect/1/app/module/dynamic`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Confluence v1 - Register modules"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/atlassian-connect/1/app/module/dynamic
Authorization: {{service.auth_token}}
Content-Type: */*

{{param:body}}
```

## Parameters

- `body` (body, string, required) — Request body (*/*).

## Original description

Registers a list of modules. For the list of modules that support dynamic registration, see [Dynamic modules](https://developer.atlassian.com/cloud/confluence/dynamic-modules/).

**[Permissions](#permissions) required:** Only Connect apps can make this request.
