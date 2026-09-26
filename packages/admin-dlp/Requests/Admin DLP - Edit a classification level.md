---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/classification-level
  - api/operation/update
  - api/effect/write
up: "[[MCP - Admin DLP]]"
app: "Admin DLP"
method: PUT
path: "/orgs/{orgId}/classification-levels/{levelId}"
category: "Classification Level"
writes_data: true
---
# Admin DLP - Edit a classification level

**Edit a classification level** — `PUT /orgs/{orgId}/classification-levels/{levelId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin DLP - Edit a classification level"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/dlp/rest/

```http
PUT https://api.atlassian.com/admin/dlp/v1/orgs/{{service.org_id}}/classification-levels/{{param:levelId}}
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `levelId` (path, string, required) — Unique ID associated with the classification level, obtained during its creation.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Edits a [classification level](/cloud/admin/dlp/rest/intro/#classification%20level) with the supplied levelId.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:classification-levels:admin`
