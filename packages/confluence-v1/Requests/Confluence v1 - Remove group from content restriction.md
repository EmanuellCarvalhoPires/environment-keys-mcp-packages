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
path: "/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}"
category: "Content restrictions"
writes_data: true
tool_note: "[[confluence_v1_remove_group_from_content_restriction]]"
---
# Confluence v1 - Remove group from content restriction

**Remove group from content restriction** — `DELETE /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}`

- Run by the tool [[confluence_v1_remove_group_from_content_restriction]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction/byOperation/{{param:operationKey}}/byGroupId/{{param:groupId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that the restriction applies to.
- `operationKey` (path, string, required) — The operation that the restriction applies to.
- `groupId` (path, string, required) — The id of the group to remove from the content restriction.

## Original description

Removes a group from a content restriction. That is, remove read or update
permission for the group for a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the content.
