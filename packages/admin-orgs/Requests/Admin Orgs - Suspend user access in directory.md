---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/users
  - api/operation/action
  - api/effect/write
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v2/orgs/{orgId}/directories/{directoryId}/users/{accountId}/suspend"
category: "Users"
writes_data: true
---
# Admin Orgs - Suspend user access in directory

**Suspend user access in directory** — `POST /v2/orgs/{orgId}/directories/{directoryId}/users/{accountId}/suspend`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Suspend user access in directory"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/users/{{param:accountId}}/suspend
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `directoryId` (path, string, required) — A directory has a unique ID. Use the Get directories endpoint to find the directory ID.
- `accountId` (path, string, required) — Every user has a unique ID. Find a user’s account ID by using the Get users endpoint.

## Original description

Suspend a user’s access in a directory to remove their access to apps temporarily. You’re not billed for a user when their access is suspended. They regain their roles and group memberships when you restore their access.
