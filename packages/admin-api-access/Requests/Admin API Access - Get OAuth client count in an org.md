---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/oauth-client
  - api/operation/search
  - api/effect/read
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: POST
path: "/orgs/{orgId}/oauth-clients/count"
category: "OAuth Client"
writes_data: false
---
# Admin API Access - Get OAuth client count in an org

**Get OAuth client count in an org** — `POST /orgs/{orgId}/oauth-clients/count`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - Get OAuth client count in an org"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
POST https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/oauth-clients/count
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Original description

Gets the count of OAuth clients in the specified organization.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `read:service-accounts-tokens:admin`
