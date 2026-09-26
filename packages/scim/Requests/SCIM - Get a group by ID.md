---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/groups
  - api/operation/get
  - api/effect/read
up: "[[MCP - SCIM]]"
app: "SCIM"
method: GET
path: "/scim/directory/{directoryId}/Groups/{id}"
category: "Groups"
writes_data: false
---
# SCIM - Get a group by ID

**Get a group by ID** — `GET /scim/directory/{directoryId}/Groups/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"SCIM - Get a group by ID"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
GET https://api.atlassian.com/scim/directory/{{param:directoryId}}/Groups/{{param:id}}
Authorization: {{service.scim_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `id` (path, string, required) — Unique SCIM id that serves as reference to the group. Use the Get groups API to get the SCIM id.

## Original description

Gets the details of a group based on the id.
