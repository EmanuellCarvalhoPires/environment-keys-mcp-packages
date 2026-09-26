---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/groups
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/memberships"
category: "Groups"
writes_data: true
---
# Admin Orgs - Add user to group

**Add user to group** — `POST /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}/memberships`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Add user to group"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/groups/{{param:groupId}}/memberships
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `directoryId` (path, string, required) — A directory has a unique ID. Use the Get directories endpoint to find the directory ID.
- `groupId` (path, string, required) — A group has a unique ID. Use the Get groups endpoint to find the group ID.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Add a user to a group. This gives the user the same app access and permissions as the group. The user must be in the same directory as the group.

**Note:** Adding a user to the org-admins group through this API no longer grants organization admin access. To assign organization admin access, use the [Assign organization-level role endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-v1-orgs-orgid-users-userid-role-assignments-assign-post) instead. This change applies to all organizations. For more information, see this [community post](https://community.atlassian.com/forums/discussion/3287720/coming-soon-use-direct-assignment-for-organization-admin-access).

You can’t add a user to a group synced from an identity provider. Manage this group in your identity provider instead.

You can’t add a user to a group if you’ve exceeded your user limit for an app that the group grants access to. Increase your user limit or suspend another user from the app first.
