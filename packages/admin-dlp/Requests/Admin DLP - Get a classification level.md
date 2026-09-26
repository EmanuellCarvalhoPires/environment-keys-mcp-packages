---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/classification-level
  - api/operation/get
  - api/effect/read
up: "[[MCP - Admin DLP]]"
app: "Admin DLP"
method: GET
path: "/orgs/{orgId}/classification-levels/{levelId}"
category: "Classification Level"
writes_data: false
---
# Admin DLP - Get a classification level

**Get a classification level** — `GET /orgs/{orgId}/classification-levels/{levelId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin DLP - Get a classification level"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/dlp/rest/

```http
GET https://api.atlassian.com/admin/dlp/v1/orgs/{{service.org_id}}/classification-levels/{{param:levelId}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `levelId` (path, string, required) — Unique ID associated with the classification level obtained during its creation.

## Original description

Gets a [classification level](/cloud/admin/dlp/rest/intro/#classification%20level) with the supplied levelId.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:classification-levels:admin`
