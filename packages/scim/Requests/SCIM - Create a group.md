---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/groups
  - api/operation/create
  - api/effect/write
up: "[[MCP - SCIM]]"
app: "SCIM"
method: POST
path: "/scim/directory/{directoryId}/Groups"
category: "Groups"
writes_data: true
---
# SCIM - Create a group

**Create a group** — `POST /scim/directory/{directoryId}/Groups`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"SCIM - Create a group"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
POST https://api.atlassian.com/scim/directory/{{param:directoryId}}/Groups
Authorization: {{service.scim_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a read-only group in the organization's directory. You can only edit groups from your identity provider. 

**Note:** An attempt to create a group with an existing name will fail with a 409 (Conflict) error.
