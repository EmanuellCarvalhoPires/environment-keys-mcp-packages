---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/admin-apis
  - api/operation/list
  - api/effect/read
up: "[[MCP - SCIM]]"
app: "SCIM"
method: GET
path: "/admin/user-provisioning/v1/org/{orgId}/user/{aaId}/get-scim-links"
category: "Admin APIs"
writes_data: false
---
# SCIM - Get SCIM links for an account

**Get SCIM links for an account** — `GET /admin/user-provisioning/v1/org/{orgId}/user/{aaId}/get-scim-links`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"SCIM - Get SCIM links for an account"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
GET https://api.atlassian.com/admin/user-provisioning/v1/org/{{service.org_id}}/user/{{param:aaId}}/get-scim-links
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `aaId` (path, string, required) — Unique ID of the user's account. The AAID can either be found in the URL of a user's profile, when browsing in the "Users" tab or the "Managed Users" tab or use the Get Users API to get the AAID.

## Original description

Get SCIM Links for a Atlassian Account ID (AAID).
