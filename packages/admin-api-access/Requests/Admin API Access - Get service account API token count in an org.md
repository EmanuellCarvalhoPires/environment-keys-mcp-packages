---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/api-token
  - api/operation/search
  - api/effect/read
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: POST
path: "/orgs/{orgId}/service-accounts/count"
category: "API Token"
writes_data: false
---
# Admin API Access - Get service account API token count in an org

**Get service account API token count in an org** — `POST /orgs/{orgId}/service-accounts/count`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - Get service account API token count in an org"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
POST https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/service-accounts/count
Authorization: {{service.admin_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Gets count of API tokens for specified service accounts within an organization.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:service-accounts-tokens:admin`
