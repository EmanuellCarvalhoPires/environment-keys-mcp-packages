---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/users
  - api/operation/create
  - api/effect/write
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v2/orgs/{orgId}/users/invite"
category: "Users"
writes_data: true
---
# Admin Orgs - Invite users to an organization

**Invite users to an organization** — `POST /v2/orgs/{orgId}/users/invite`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Invite users to an organization"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/users/invite
Authorization: {{service.admin_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Invite people to your organization. When you invite someone:
- they’re given app roles according to your invitation.
- they’re added to directories based on apps in your invitation.
- they’re added to groups according to your invitation.
- they receive an email invitation if the `sendNotification` field is set to `true` and the `notificationText` field contains a message to include in the email invitation.

**This API is only available to customers who have at least one paid subscription in their organization.**
