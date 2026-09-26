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
path: "/orgs/{orgId}/classification-levels/publish"
category: "Classification Level"
writes_data: true
---
# Admin DLP - Publish classification level(s)

**Publish classification level(s)** — `POST /orgs/{orgId}/classification-levels/publish`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin DLP - Publish classification level(s)"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/dlp/rest/

```http
POST https://api.atlassian.com/admin/dlp/v1/orgs/{{service.org_id}}/classification-levels/publish
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Publishes one or more [classification level](/cloud/admin/dlp/rest/intro/#classification%20level) with the supplied levelIds.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:classification-levels:admin`
