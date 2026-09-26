---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/lifecycle
  - api/operation/action
  - api/effect/write
up: "[[MCP - Admin Users]]"
app: "Admin Users"
method: POST
path: "/users/{account_id}/manage/lifecycle/enable"
category: "Lifecycle"
writes_data: true
---
# Admin Users - Activate a user

**Activate a user** — `POST /users/{account_id}/manage/lifecycle/enable`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Users - Activate a user"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-management/rest/

```http
POST https://api.atlassian.com/users/{{param:account_id}}/manage/lifecycle/enable
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `account_id` (path, string, required) — The unique identifier of the user to activate.

## Original description

Activates the specified user account. The permission to make use of this resource is exposed by the
`lifecycle.enablement` privilege.

User accounts that were deactivated due to US export controls cannot be reactivated using this API. If you believe
the account was incorrectly blocked, please contact [Atlassian Support](https://support.atlassian.com/contact).

User accounts that have been deleted need the deletion to be canceled before reactivating.
