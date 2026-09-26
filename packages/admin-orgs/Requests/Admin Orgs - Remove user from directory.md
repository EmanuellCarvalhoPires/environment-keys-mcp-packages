---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/users
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: DELETE
path: "/v2/orgs/{orgId}/directories/{directoryId}/users/{accountId}"
category: "Users"
writes_data: true
---
# Admin Orgs - Remove user from directory

**Remove user from directory** — `DELETE /v2/orgs/{orgId}/directories/{directoryId}/users/{accountId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Remove user from directory"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
DELETE https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/users/{{param:accountId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `directoryId` (path, string, required) — A directory has a unique ID. Use the Get directories endpoint to find the directory ID.
- `accountId` (path, string, required) — Every user has a unique ID. Find a user’s account ID by using the Get users endpoint.

## Original description

Remove a user from a directory if you don’t want them to appear in your directory or have access to your apps anymore. You’re not billed for a user once they’re removed.
You must invite the user to your organization again if you want to reinstate their access to your apps. You’ll need to assign their roles and group memberships again.
