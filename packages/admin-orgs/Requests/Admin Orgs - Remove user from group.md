---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/groups
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: DELETE
path: "/v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/memberships/{accountId}"
category: "Groups"
writes_data: true
---
# Admin Orgs - Remove user from group

**Remove user from group** — `DELETE /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/memberships/{accountId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Remove user from group"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
DELETE https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/groups/{{param:groupId}}/memberships/{{param:accountId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `directoryId` (path, string, required) — A directory has a unique ID. Use the Get directories endpoint to find the directory ID.
- `groupId` (path, string, required) — A group has a unique ID. Use the Get groups endpoint to find the group ID.
- `accountId` (path, string, required) — Every user has a unique ID. Find a user’s account ID by using the Get users endpoint.

## Original description

Remove a user from a group. This removes any app access and permissions granted by this group, but the user may still be in other groups that grant the same app access and permissions.

**Note:** Removing a user from the org-admins group through this API will no longer revoke organization admin access. To revoke the organization admin role, use the [Remove organization-level role endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-v1-orgs-orgid-users-userid-role-assignments-revoke-post) instead. This applies to all organizations. For more information, see this [community post](https://community.atlassian.com/forums/discussion/3287720/coming-soon-use-direct-assignment-for-organization-admin-access).
