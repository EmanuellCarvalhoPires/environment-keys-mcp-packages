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
path: "/users/{account_id}/manage/lifecycle/cancel-delete"
category: "Lifecycle"
writes_data: true
---
# Admin Users - Cancel delete account

**Cancel delete account** — `POST /users/{account_id}/manage/lifecycle/cancel-delete`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Users - Cancel delete account"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-management/rest/

```http
POST https://api.atlassian.com/users/{{param:account_id}}/manage/lifecycle/cancel-delete
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `account_id` (path, string, required) — Unique ID of the user's account that you are deleting. Use the Get users in an organization API to get the accountId.

## Original description

This API will:
 - Cancel the scheduled deletion of the specified managed account.
 - Restore and activate the user’s account.
 
 Specifications:
 - You can cancel the deletion within the 14-day grace period of deleting a managed account. After that the account is permanently deleted.
 
 The permission to make use of this resource is exposed by the `lifecycle.delete` privilege. Learn more about [Get user management permissions API](https://developer.atlassian.com/cloud/admin/user-management/rest/api-group-manage/#api-users-account-id-manage-get) to manage the specified user.
