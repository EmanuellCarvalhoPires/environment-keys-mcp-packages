---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/authentication-policies
  - api/operation/get
  - api/effect/read
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: GET
path: "/admin/control/v1/orgs/{orgId}/auth-policy/task/{taskId}"
category: "Authentication Policies"
writes_data: false
---
# Admin Control - Get the status of a task

**Get the status of a task** — `GET /admin/control/v1/orgs/{orgId}/auth-policy/task/{taskId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Control - Get the status of a task"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
GET https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/auth-policy/task/{{param:taskId}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `taskId` (path, string, required) — Unique Id obtained after adding users to an authentication policy.

## Original description

Verify that users are assigned to the intended policy and report errors, if any.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:policies:admin`
