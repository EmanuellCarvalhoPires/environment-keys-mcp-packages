---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/schemas
  - api/operation/list
  - api/effect/read
up: "[[MCP - SCIM]]"
app: "SCIM"
method: GET
path: "/scim/directory/{directoryId}/Schemas"
category: "Schemas"
writes_data: false
---
# SCIM - Get all schemas

**Get all schemas** — `GET /scim/directory/{directoryId}/Schemas`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"SCIM - Get all schemas"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
GET https://api.atlassian.com/scim/directory/{{param:directoryId}}/Schemas
Authorization: {{service.scim_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.

## Original description

Get all SCIM features metadata of your organization. 

**Note:** This API does not support filtering, pagination, or sorting.
