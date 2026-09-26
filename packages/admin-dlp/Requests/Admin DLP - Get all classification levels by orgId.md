---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/classification-level
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin DLP]]"
app: "Admin DLP"
method: GET
path: "/orgs/{orgId}/classification-levels"
category: "Classification Level"
writes_data: false
---
# Admin DLP - Get all classification levels by orgId

**Get all classification levels by orgId** — `GET /orgs/{orgId}/classification-levels`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin DLP - Get all classification levels by orgId"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/dlp/rest/

```http
GET https://api.atlassian.com/admin/dlp/v1/orgs/{{service.org_id}}/classification-levels
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Original description

Gets all [classification levels](/cloud/admin/dlp/rest/intro/#classification%20level) in an organization.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:classification-levels:admin`
