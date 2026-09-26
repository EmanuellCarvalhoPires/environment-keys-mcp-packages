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
path: "/v1/orgs/{orgId}/policies/{policyId}/resources"
category: "Policies"
writes_data: true
---
# Admin Orgs - Add Resource to Policy

**Add Resource to Policy** — `POST /v1/orgs/{orgId}/policies/{policyId}/resources`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Add Resource to Policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}/resources
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `policyId` (path, string, required) — ID of the policy to query
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds a resource to an existing Policy
