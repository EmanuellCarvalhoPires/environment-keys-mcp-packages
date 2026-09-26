---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/schemas
  - api/operation/get
  - api/effect/read
up: "[[MCP - SCIM]]"
app: "SCIM"
method: GET
path: "/scim/directory/{directoryId}/Schemas/urn{ietf}{params}{scim}{schemas}{extension}{enterprise}:2.0{User}"
category: "Schemas"
writes_data: false
---
# SCIM - Get user enterprise extension schemas

**Get user enterprise extension schemas** — `GET /scim/directory/{directoryId}/Schemas/urn{ietf}{params}{scim}{schemas}{extension}{enterprise}:2.0{User}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"SCIM - Get user enterprise extension schemas"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
GET https://api.atlassian.com/scim/directory/{{param:directoryId}}/Schemas/urn{{param:ietf}}{{param:params}}{{param:scim}}{{param:schemas}}{{param:extension}}{{param:enterprise}}:2.0{{param:User}}
Authorization: {{service.scim_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `ietf` (path, string, required) — Value of ietf in the path.
- `params` (path, string, required) — Value of params in the path.
- `scim` (path, string, required) — Value of scim in the path.
- `schemas` (path, string, required) — Value of schemas in the path.
- `extension` (path, string, required) — Value of extension in the path.
- `enterprise` (path, string, required) — Value of enterprise in the path.
- `User` (path, string, required) — Value of User in the path.

## Original description

Get the user enterprise extension schemas from the SCIM provider. 

**Note:** This API does not support filtering, pagination, or sorting.
