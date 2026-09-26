---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/groups
  - api/operation/create
  - api/effect/write
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v2/orgs/{orgId}/directories/{directoryId}/groups"
category: "Groups"
writes_data: true
---
# Admin Orgs - Create group

**Create group** — `POST /v2/orgs/{orgId}/directories/{directoryId}/groups`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Create group"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/groups
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `directoryId` (path, string, required) — A directory has a unique ID. Use the Get directories endpoint to find the directory ID.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a group in a directory to manage app access and permissions for multiple users together.
