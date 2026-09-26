---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}"
category: "Content restrictions"
writes_data: true
tool_note: "[[confluence_v1_add_group_to_content_restriction]]"
---
# Confluence v1 - Add group to content restriction

**Add group to content restriction** — `PUT /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}`

- Run by the tool [[confluence_v1_add_group_to_content_restriction]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction/byOperation/{{param:operationKey}}/byGroupId/{{param:groupId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that the restriction applies to.
- `operationKey` (path, string, required) — The operation that the restriction applies to.
- `groupId` (path, string, required) — The groupId of the group to add to the content restriction.

## Original description

Adds a group to a content restriction by Group Id. That is, grant read or update
permission to the group for a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the content.
