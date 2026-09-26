---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v2/orgs/{orgId}/directories/{directoryId}/users/stats"
category: "Users"
writes_data: false
---
# Admin Orgs - Get user stats in an organization

**Get user stats in an organization** — `GET /v2/orgs/{orgId}/directories/{directoryId}/users/stats`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get user stats in an organization"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/users/stats
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — Unique ID associated with a directory. The - character can be used to increase the operation scope to all directories the requestor has permission to manage.

## Original description

Return user stats for the organization.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:directories:admin`
