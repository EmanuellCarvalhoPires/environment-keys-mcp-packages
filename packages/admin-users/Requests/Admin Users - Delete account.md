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
path: "/users/{account_id}/manage/lifecycle/delete"
category: "Lifecycle"
writes_data: true
---
# Admin Users - Delete account

**Delete account** — `POST /users/{account_id}/manage/lifecycle/delete`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Users - Delete account"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-management/rest/

```http
POST https://api.atlassian.com/users/{{param:account_id}}/manage/lifecycle/delete
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `account_id` (path, string, required) — Unique ID of the user's account that you are deleting. Use the Get users in an organization API to get the accountId.

## Original description

This API will:
- Delete a managed account from Atlassian Administration.
- Withdraw complete access to all products and services listed in Atlassian Administration.
- Remove reference to the account from all lists under Directory in Atlassian Administration.

Specifications:
- Deleting an account is permanent. If you think you’ll need the account again, we recommend you [deactivate](https://support.atlassian.com/user-management/docs/deactivate-a-managed-account/) it instead.
- Before you permanently delete the account, you’ll have a 14-day grace period, during which the account will appear as temporarily deactivated.

Learn more about [deleting a managed account](https://support.atlassian.com/user-management/docs/delete-a-managed-account/).

Learn the fastest way to get the paramaters and delete account with a detailed [tutorial](https://developer.atlassian.com/cloud/admin/user-management/delete-managed-account/#delete-account). 

The permission to make use of this resource is exposed by the `lifecycle.delete` privilege. Learn more about [Get user management permissions API](https://developer.atlassian.com/cloud/admin/user-management/rest/api-group-manage/#api-users-account-id-manage-get) to manage the specified user.
