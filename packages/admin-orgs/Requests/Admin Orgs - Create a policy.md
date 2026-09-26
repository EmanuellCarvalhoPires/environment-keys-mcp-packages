---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/create
  - api/effect/write
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v1/orgs/{orgId}/policies"
category: "Policies"
writes_data: true
---
# Admin Orgs - Create a policy

**Create a policy** — `POST /v1/orgs/{orgId}/policies`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Create a policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/policies
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a policy for an org
