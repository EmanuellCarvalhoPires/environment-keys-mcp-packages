---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/users
  - api/operation/get
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v2/orgs/{orgId}/directories/{directoryId}/users/{userId}"
category: "Users"
writes_data: false
---
# Admin Orgs - Get details of a user in a directory

**Get details of a user in a directory** — `GET /v2/orgs/{orgId}/directories/{directoryId}/users/{userId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get details of a user in a directory"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/users/{{param:userId}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — Unique ID associated with a directory. The - character can be used to increase the operation scope to all directories the requestor has permission to manage.
- `userId` (path, string, required) — Value of userId in the path.

## Original description

Returns detailed information about a specific user in a directory within an organization.
