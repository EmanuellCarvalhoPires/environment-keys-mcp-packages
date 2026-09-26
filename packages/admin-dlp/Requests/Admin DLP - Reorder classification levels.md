---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/classification-level
  - api/operation/action
  - api/effect/write
up: "[[MCP - Admin DLP]]"
app: "Admin DLP"
method: POST
path: "/orgs/{orgId}/classification-levels/reorder"
category: "Classification Level"
writes_data: true
---
# Admin DLP - Reorder classification levels

**Reorder classification levels** — `POST /orgs/{orgId}/classification-levels/reorder`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin DLP - Reorder classification levels"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/dlp/rest/

```http
POST https://api.atlassian.com/admin/dlp/v1/orgs/{{service.org_id}}/classification-levels/reorder
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Changes the order of [classification levels](/cloud/admin/dlp/rest/intro/#classification%20level). The most sensitive classification level should be ranked 1.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:classification-levels:admin`
