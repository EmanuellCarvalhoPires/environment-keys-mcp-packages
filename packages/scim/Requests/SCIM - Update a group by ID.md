---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/groups
  - api/operation/update
  - api/effect/write
up: "[[MCP - SCIM]]"
app: "SCIM"
method: PUT
path: "/scim/directory/{directoryId}/Groups/{id}"
category: "Groups"
writes_data: true
---
# SCIM - Update a group by ID

**Update a group by ID** — `PUT /scim/directory/{directoryId}/Groups/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"SCIM - Update a group by ID"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
PUT https://api.atlassian.com/scim/directory/{{param:directoryId}}/Groups/{{param:id}}
Authorization: {{service.scim_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `id` (path, string, required) — Unique SCIM id that serves as reference to the group. Use the [Get groups API] (https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-groups/api-scim-directory-directoryid-group…
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the details of a group with its unique ID.
