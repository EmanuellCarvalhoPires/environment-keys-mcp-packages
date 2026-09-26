---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user"
category: "Content restrictions"
writes_data: true
tool_note: "[[confluence_v1_remove_user_from_content_restriction]]"
---
# Confluence v1 - Remove user from content restriction

**Remove user from content restriction** — `DELETE /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user`

- Run by the tool [[confluence_v1_remove_user_from_content_restriction]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction/byOperation/{{param:operationKey}}/user?key={{param:key}}&username={{param:username}}&accountId={{param:accountId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that the restriction applies to.
- `operationKey` (path, string, required) — The operation that the restriction applies to.
- `key` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details.
- `username` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details.
- `accountId` (query, string, optional) — The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192.

## Original description

Removes a group from a content restriction. That is, remove read or update
permission for the group for a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the content.
