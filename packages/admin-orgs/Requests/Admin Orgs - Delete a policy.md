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
path: "/v1/orgs/{orgId}/policies/{policyId}"
category: "Policies"
writes_data: true
---
# Admin Orgs - Delete a policy

**Delete a policy** — `DELETE /v1/orgs/{orgId}/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Delete a policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
DELETE https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `policyId` (path, string, required) — ID of the policy to delete

## Original description

Delete a policy for an org
