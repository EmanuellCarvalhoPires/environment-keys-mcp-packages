---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/service-account
  - api/operation/update
  - api/effect/write
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: PATCH
path: "/orgs/{orgId}/service-accounts"
category: "Service Account"
writes_data: true
---
# Admin API Access - Update a service account

**Update a service account** — `PATCH /orgs/{orgId}/service-accounts`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin API Access - Update a service account"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
PATCH https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/service-accounts
Authorization: {{service.admin_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates a service account's display name and/or description within the specified organization.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `write:service-accounts:admin`
