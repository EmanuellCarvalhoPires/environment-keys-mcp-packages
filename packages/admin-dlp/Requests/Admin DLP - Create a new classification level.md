---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/classification-level
  - api/operation/create
  - api/effect/write
up: "[[MCP - Admin DLP]]"
app: "Admin DLP"
method: POST
path: "/orgs/{orgId}/classification-levels"
category: "Classification Level"
writes_data: true
---
# Admin DLP - Create a new classification level

**Create a new classification level** — `POST /orgs/{orgId}/classification-levels`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin DLP - Create a new classification level"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/dlp/rest/

```http
POST https://api.atlassian.com/admin/dlp/v1/orgs/{{service.org_id}}/classification-levels
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a draft [classification level](cloud/admin/dlp/rest/intro/#classification%20level) for an organization.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:classification-levels:admin`
