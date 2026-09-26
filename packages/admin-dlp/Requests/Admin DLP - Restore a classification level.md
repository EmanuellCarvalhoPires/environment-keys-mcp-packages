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
path: "/orgs/{orgId}/classification-levels/restore"
category: "Classification Level"
writes_data: true
---
# Admin DLP - Restore a classification level

**Restore a classification level** — `POST /orgs/{orgId}/classification-levels/restore`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin DLP - Restore a classification level"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/dlp/rest/

```http
POST https://api.atlassian.com/admin/dlp/v1/orgs/{{service.org_id}}/classification-levels/restore
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Restores a [classification level](/cloud/admin/dlp/rest/intro/#classification%20level) with supplied levelId. When you restore an archived classification level, it’s restored as a draft. 

When you’re ready for your users to start classifying Confluence pages and Jira issues, you can publish the classification level.

If the classification level had been published before being archived, restored, and published again, any pages and issues classified at this level before it was archived will regain this classification level.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:classification-levels:admin`
