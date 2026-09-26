---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v1/orgs/{orgId}/policies/{policyId}/validate"
category: "Policies"
writes_data: false
---
# Admin Orgs - Validate Policy

**Validate Policy** — `GET /v1/orgs/{orgId}/policies/{policyId}/validate`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Validate Policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}/validate
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `policyId` (path, string, required) — Policy ID

## Original description

Validate a policy based on specific requirements. For example, Trigger CDEN validation by pushing a task into the SQS dns-validation queue
