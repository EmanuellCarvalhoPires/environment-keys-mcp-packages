---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/service-account
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: GET
path: "/orgs/{orgId}/service-accounts"
category: "Service Account"
writes_data: false
---
# Admin API Access - List service accounts in an org

**List service accounts in an org** — `GET /orgs/{orgId}/service-accounts`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - List service accounts in an org"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
GET https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/service-accounts
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Original description

Retrieves all service accounts for the specified organization.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `read:service-accounts:admin`
