---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permission-transition
  - api/operation/action
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/space-permissions/transition/access-removals"
category: "Space Permission Transition"
writes_data: true
tool_note: "[[confluence_bulk_remove_space_permission_access]]"
---
# Confluence v2 - Bulk remove space permission access

**Bulk remove space permission access** — `POST /space-permissions/transition/access-removals`

- Run by the tool [[confluence_bulk_remove_space_permission_access]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/space-permissions/transition/access-removals
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Bulk removes access for one or more permission combination IDs obtained from the space permission
combinations. This removes all space permissions for the specified combinations across
the targeted spaces.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be a Confluence administrator.
