---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dynamic-modules
  - api/operation/delete
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/atlassian-connect/1/app/module/dynamic"
category: "Dynamic modules"
writes_data: true
---
# Jira v3 - Remove modules

**Remove modules** — `DELETE /rest/atlassian-connect/1/app/module/dynamic`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Remove modules"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/atlassian-connect/1/app/module/dynamic?moduleKey={{param:moduleKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `moduleKey` (query, string, optional) — The key of the module to remove. To include multiple module keys, provide multiple copies of this parameter. For example, moduleKey=dynamic-attachment-entity-property&moduleKey=dynamic-select-field.

## Original description

Remove all or a list of modules registered by the calling app.

**[Permissions](#permissions) required:** Only Connect apps can make this request.
