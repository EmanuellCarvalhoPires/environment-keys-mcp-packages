---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/oauth-client
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: GET
path: "/orgs/{orgId}/oauth-clients"
category: "OAuth Client"
writes_data: false
---
# Admin API Access - Get all OAuth clients in an org

**Get all OAuth clients in an org** — `GET /orgs/{orgId}/oauth-clients`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - Get all OAuth clients in an org"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
GET https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/oauth-clients?pageSize={{param:pageSize}}&cursor={{param:cursor}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `pageSize` (query, string, optional) — Select the number of OAuth client records to include in the results.
- `cursor` (query, string, optional) — Navigate to a specific page of paginated results. In a given response, it may include a self, next, and prev cursor to fetch the respective set of paginated results.

## Original description

Retrieves all OAuth clients for the specified organization.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `read:service-accounts-tokens:admin`
