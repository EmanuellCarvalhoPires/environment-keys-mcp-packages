---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/admin-apis
  - api/operation/search
  - api/effect/read
up: "[[MCP - SCIM]]"
app: "SCIM"
method: POST
path: "/admin/user-provisioning/v1/org/{orgId}/get-scim-links-for-email"
category: "Admin APIs"
writes_data: false
---
# SCIM - Get SCIM Links for an email

**Get SCIM Links for an email** — `POST /admin/user-provisioning/v1/org/{orgId}/get-scim-links-for-email`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"SCIM - Get SCIM Links for an email"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
POST https://api.atlassian.com/admin/user-provisioning/v1/org/{{service.org_id}}/get-scim-links-for-email
Authorization: {{service.admin_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Get SCIM Links for an email address in an organization.
