---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/authentication-policies
  - api/operation/search
  - api/effect/read
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: POST
path: "/admin/control/v1/orgs/{orgId}/users/auth-policies/bulk-fetch"
category: "Authentication Policies"
writes_data: false
---
# Admin Control - Get policy information for managed users

**Get policy information for managed users** — `POST /admin/control/v1/orgs/{orgId}/users/auth-policies/bulk-fetch`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Control - Get policy information for managed users"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
POST https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/users/auth-policies/bulk-fetch
Authorization: {{service.admin_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Get authentication policy information for a given list of managed users. This is a bulk action.
