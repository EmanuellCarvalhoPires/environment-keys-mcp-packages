---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/groups
  - api/operation/get
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}"
category: "Groups"
writes_data: false
---
# Admin Orgs - Get group details

**Get group details** — `GET /v2/orgs/{orgId}/directories/{directoryId}/groups/{groupId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get group details"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/groups/{{param:groupId}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — Unique ID associated with a directory. The - character can be used to increase the operation scope to all directories the requestor has permission to manage.
- `groupId` (path, string, required) — Unique ID associated with a group.

## Original description

Returns the details of a group.
