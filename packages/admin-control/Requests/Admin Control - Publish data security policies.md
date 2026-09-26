---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/action
  - api/effect/write
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: POST
path: "/admin/control/v2/orgs/{orgId}/policies/publishDraftPolicies"
category: "Policies"
writes_data: true
---
# Admin Control - Publish data security policies

**Publish data security policies** — `POST /admin/control/v2/orgs/{orgId}/policies/publishDraftPolicies`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Control - Publish data security policies"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
POST https://api.atlassian.com/admin/control/v2/orgs/{{service.org_id}}/policies/publishDraftPolicies
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Publishes policies by a bulk request for a specific ruleName. This is the only way to create or modify published policies.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:policies:admin`
