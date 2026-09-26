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
path: "/space-permissions/transition/role-assignments"
category: "Space Permission Transition"
writes_data: true
tool_note: "[[confluence_bulk_assign_space_permission_roles]]"
---
# Confluence v2 - Bulk assign space permission roles

**Bulk assign space permission roles** — `POST /space-permissions/transition/role-assignments`

- Run by the tool [[confluence_bulk_assign_space_permission_roles]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/space-permissions/transition/role-assignments
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Bulk assigns roles for one or more permission combination IDs obtained from the space permission
combinations. Supports targeting all spaces, specific spaces, or excluding specific spaces.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be a Confluence administrator.
