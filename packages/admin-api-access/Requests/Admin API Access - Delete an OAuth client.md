---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/oauth-client
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: DELETE
path: "/orgs/{orgId}/oauth-clients/{clientId}"
category: "OAuth Client"
writes_data: true
---
# Admin API Access - Delete an OAuth client

**Delete an OAuth client** — `DELETE /orgs/{orgId}/oauth-clients/{clientId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin API Access - Delete an OAuth client"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
DELETE https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/oauth-clients/{{param:clientId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `clientId` (path, string, required) — The unique identifier of the OAuth client to delete.

## Original description

Deletes an existing OAuth client from the specified organization.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `delete:service-accounts-tokens:admin`
