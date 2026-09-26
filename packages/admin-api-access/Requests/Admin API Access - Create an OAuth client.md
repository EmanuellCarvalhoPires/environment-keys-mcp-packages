---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/oauth-client
  - api/operation/create
  - api/effect/write
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: POST
path: "/orgs/{orgId}/oauth-clients"
category: "OAuth Client"
writes_data: true
---
# Admin API Access - Create an OAuth client

**Create an OAuth client** — `POST /orgs/{orgId}/oauth-clients`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin API Access - Create an OAuth client"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
POST https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/oauth-clients
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new OAuth client for the specified organization.

> **Note:** This is a session-only endpoint and cannot be called with an API token or OAuth 2.0 scope. It requires an active admin session with org management permissions.

#### Scopes
This endpoint is session-only and does not accept OAuth 2.0 scopes.
