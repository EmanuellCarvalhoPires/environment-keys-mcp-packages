---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/groups
  - api/operation/action
  - api/effect/write
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/role-assignments/revoke"
category: "Groups"
writes_data: true
---
# Admin Orgs - Remove access from group

**Remove access from group** — `POST /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/role-assignments/revoke`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Remove access from group"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/groups/{{param:groupId}}/role-assignments/revoke
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `directoryId` (path, string, required) — A directory has a unique ID. Use the Get directories endpoint to find the directory ID.
- `groupId` (path, string, required) — A group has a unique ID. Use the Get groups endpoint to find the group ID.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Revoke a role from a group to remove access to an app from all members. A member can still access the app if they’re in another group that grants access to the same app.
