---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/groups
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: DELETE
path: "/v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}"
category: "Groups"
writes_data: true
---
# Admin Orgs - Delete group

**Delete group** — `DELETE /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Delete group"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
DELETE https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/groups/{{param:groupId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `directoryId` (path, string, required) — A directory has a unique ID. Use the Get directories endpoint to find the directory ID.
- `groupId` (path, string, required) — A group has a unique ID. Use the Get groups endpoint to find the group ID.

## Original description

Delete a group from a directory if you don’t need this group anymore. This removes any app access and permissions granted by this group from all members. A member can still access an app if they’re in another group that grants access to the same app.
