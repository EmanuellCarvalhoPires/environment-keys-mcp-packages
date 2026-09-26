---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/service-account
  - api/operation/create
  - api/effect/write
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: POST
path: "/orgs/{orgId}/service-accounts"
category: "Service Account"
writes_data: true
---
# Admin API Access - Create a service account

**Create a service account** — `POST /orgs/{orgId}/service-accounts`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin API Access - Create a service account"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
POST https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/service-accounts
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new service account for the specified organization. The service account is created with the given display name and optional description, then invited with the specified permission rules and optional additional group memberships.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `write:service-accounts:admin`
