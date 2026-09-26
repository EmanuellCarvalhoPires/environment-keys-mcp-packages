---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/admin-apis
  - api/operation/delete
  - api/effect/write
up: "[[MCP - SCIM]]"
app: "SCIM"
method: DELETE
path: "/admin/user-provisioning/v1/org/{orgId}/user/{AAID}/onlyDeleteUserInDB"
category: "Admin APIs"
writes_data: true
---
# SCIM - Delete user in SCIM DB

**Delete user in SCIM DB** — `DELETE /admin/user-provisioning/v1/org/{orgId}/user/{AAID}/onlyDeleteUserInDB`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"SCIM - Delete user in SCIM DB"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
DELETE https://api.atlassian.com/admin/user-provisioning/v1/org/{{service.org_id}}/user/{{param:AAID}}/onlyDeleteUserInDB
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `AAID` (path, string, required) — Unique ID of the user's account. The AAID can either be found in the URL of a user's profile, when browsing in the "Users" tab or the "Managed Users" tab or use the Get Users API to get the AAID.

## Original description

Delete a user in our SCIM DB with a Atlassian Account ID (AAID). This will apply to all directories in your organization matching that AAID and only works for managed users. 


You will have to completely reprovision the user to their respective groups after deletion. 


Explore more about [updating managed SCIM email addresses](../../email-change/).
