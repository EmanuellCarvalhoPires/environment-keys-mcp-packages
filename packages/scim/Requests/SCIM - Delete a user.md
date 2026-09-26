---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/users
  - api/operation/delete
  - api/effect/write
up: "[[MCP - SCIM]]"
app: "SCIM"
method: DELETE
path: "/scim/directory/{directoryId}/Users/{userId}"
category: "Users"
writes_data: true
---
# SCIM - Delete a user

**Delete a user** — `DELETE /scim/directory/{directoryId}/Users/{userId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"SCIM - Delete a user"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
DELETE https://api.atlassian.com/scim/directory/{{param:directoryId}}/Users/{{param:userId}}
Authorization: {{service.scim_auth_token}}
```

## Parameters

- `directoryId` (path, string, required) — The ID assigned to your identity provider when linked to your Atlassian organization.
- `userId` (path, string, required) — Unique ID to identiy the SCIM users. Use the Get users API to get the userId.

## Original description

Deleting a user via the SCIM APIs will unlink the user from your identity provider and deactivate the user within Atlassian if they are managed by your organization.

The deleted user is not available for future requests until created with a new `userId`. If the user is deactivated they can be activated again via [Atlassian Administration](https://admin.atlassian.com/).

**Note:** Executing this API call will result in the deletion of the SCIM record, and there is no method to reverse these changes except by creating a new SCIM record with [Create a user API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-users/#api-scim-directory-directoryid-users-post).
