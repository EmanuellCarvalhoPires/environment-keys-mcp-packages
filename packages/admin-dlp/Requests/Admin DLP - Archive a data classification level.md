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
path: "/orgs/{orgId}/classification-levels/archive"
category: "Classification Level"
writes_data: true
---
# Admin DLP - Archive a data classification level

**Archive a data classification level** — `POST /orgs/{orgId}/classification-levels/archive`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin DLP - Archive a data classification level"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/dlp/rest/

```http
POST https://api.atlassian.com/admin/dlp/v1/orgs/{{service.org_id}}/classification-levels/archive
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

-
Archives a [classification level](/cloud/admin/dlp/rest/intro/#classification%20level) with the supplied levelId (batch not currently supported).
When you archive a published classification level:
- Users won’t be able to classify pages at this level
- Any page or issues classified at this level will become unclassified
- Pages and issues will retain history

In the event that the classification level is restored and published, those pages and issues will regain this classification level.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:classification-levels:admin`
