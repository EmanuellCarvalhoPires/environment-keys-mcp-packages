---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permissions
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/space/{spaceKey}/permission/custom-content"
category: "Space permissions"
writes_data: true
tool_note: "[[confluence_v1_add_new_custom_content_permission_to_space]]"
---
# Confluence v1 - Add new custom content permission to space

**Add new custom content permission to space** — `POST /wiki/rest/api/space/{spaceKey}/permission/custom-content`

- Run by the tool [[confluence_v1_add_new_custom_content_permission_to_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/permission/custom-content
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to be queried for its content.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds new custom content permission to space.

If the permission to be added is a group permission, the group can be identified
by its group name or group id.

Note: Only apps can access this REST resource and only make changes to the respective app permissions.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Admin' permission for the space.
