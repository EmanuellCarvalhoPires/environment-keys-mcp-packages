---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/dynamic-modules
  - api/operation/delete
  - api/effect/write
  - api/version/v1
  - api/restriction/app-connect
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/atlassian-connect/1/app/module/dynamic"
category: "Dynamic modules"
writes_data: true
---
# Confluence v1 - Remove modules

**Remove modules** — `DELETE /wiki/rest/atlassian-connect/1/app/module/dynamic`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Confluence v1 - Remove modules"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/atlassian-connect/1/app/module/dynamic?moduleKey={{param:moduleKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `moduleKey` (query, string, required) — The key of the module to remove. To include multiple module keys, provide multiple copies of this parameter. For example, moduleKey=dynamic-attachment-entity-property&moduleKey=dynamic-select-field.

## Original description

Remove all or a list of modules registered by the calling app.

**[Permissions](#permissions) required:** Only Connect apps can make this request.
