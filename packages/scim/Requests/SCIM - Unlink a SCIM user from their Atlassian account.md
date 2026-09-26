---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/admin-apis
  - api/operation/update
  - api/effect/write
up: "[[MCP - SCIM]]"
app: "SCIM"
method: PATCH
path: "/admin/user-provisioning/v1/org/{orgId}/scimDirectoryId/{scimDirectoryId}/scimUserId/{scimUserId}/unlink"
category: "Admin APIs"
writes_data: true
---
# SCIM - Unlink a SCIM user from their Atlassian account

**Unlink a SCIM user from their Atlassian account** — `PATCH /admin/user-provisioning/v1/org/{orgId}/scimDirectoryId/{scimDirectoryId}/scimUserId/{scimUserId}/unlink`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"SCIM - Unlink a SCIM user from their Atlassian account"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
PATCH https://api.atlassian.com/admin/user-provisioning/v1/org/{{service.org_id}}/scimDirectoryId/{{param:scimDirectoryId}}/scimUserId/{{param:scimUserId}}/unlink
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `scimDirectoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `scimUserId` (path, string, required) — The SCIM user ID to unlink. Use the Get SCIM Links for an email API to get the SCIM User ID.

## Original description

Unlinks a SCIM user from their Atlassian account without deleting the user.
