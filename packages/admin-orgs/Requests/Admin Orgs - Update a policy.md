---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/update
  - api/effect/write
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: PUT
path: "/v1/orgs/{orgId}/policies/{policyId}"
category: "Policies"
writes_data: true
---
# Admin Orgs - Update a policy

**Update a policy** — `PUT /v1/orgs/{orgId}/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Update a policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
PUT https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `policyId` (path, string, required) — ID of the policy to update
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a policy for an org
