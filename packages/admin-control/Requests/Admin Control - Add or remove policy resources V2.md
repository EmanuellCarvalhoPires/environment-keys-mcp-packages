---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/resources
  - api/operation/create
  - api/effect/write
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: POST
path: "/admin/control/v2/orgs/{orgId}/policies/{policyId}/resources"
category: "Resources"
writes_data: true
---
# Admin Control - Add or remove policy resources V2

**Add or remove policy resources V2** — `POST /admin/control/v2/orgs/{orgId}/policies/{policyId}/resources`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Control - Add or remove policy resources V2"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
POST https://api.atlassian.com/admin/control/v2/orgs/{{service.org_id}}/policies/{{param:policyId}}/resources
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `policyId` (path, string, required) — Unique Id associated with each policy.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Add or remove resources to a policy

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:policies:admin`
