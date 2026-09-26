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
path: "/wiki/rest/api/space/{spaceKey}/permission"
category: "Space permissions"
writes_data: true
tool_note: "[[confluence_v1_add_new_permission_to_space]]"
---
# Confluence v1 - Add new permission to space

**Add new permission to space** — `POST /wiki/rest/api/space/{spaceKey}/permission`

- Run by the tool [[confluence_v1_add_new_permission_to_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/permission
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to be queried for its content.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds new permission to space.

If the permission to be added is a group permission, the group can be identified
by its group name or group id.

Note: Apps cannot access this REST resource - including when utilizing user impersonation.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Admin' permission for the space.
