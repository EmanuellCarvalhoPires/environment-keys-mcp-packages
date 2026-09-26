---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: DELETE
path: "/v1/orgs/{orgId}/policies/{policyId}/resources/{resourceId}"
category: "Policies"
writes_data: true
---
# Admin Orgs - Delete Policy Resource

**Delete Policy Resource** — `DELETE /v1/orgs/{orgId}/policies/{policyId}/resources/{resourceId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Delete Policy Resource"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
DELETE https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}/resources/{{param:resourceId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `policyId` (path, string, required) — ID of the policy to query
- `resourceId` (path, string, required) — Resource ID

## Original description

Delete an existing Policy Resource
