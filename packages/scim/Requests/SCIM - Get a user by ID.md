---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/users
  - api/operation/get
  - api/effect/read
up: "[[MCP - SCIM]]"
app: "SCIM"
method: GET
path: "/scim/directory/{directoryId}/Users/{userId}"
category: "Users"
writes_data: false
---
# SCIM - Get a user by ID

**Get a user by ID** — `GET /scim/directory/{directoryId}/Users/{userId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"SCIM - Get a user by ID"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
GET https://api.atlassian.com/scim/directory/{{param:directoryId}}/Users/{{param:userId}}?attributes={{param:attributes}}&excludedAttributes={{param:excludedAttributes}}
Authorization: {{service.scim_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `userId` (path, string, required) — Unique ID to identiy the users. Use the Get users API to get the userId.
- `attributes` (query, string, optional) — Resource attributes to be included in response. Mutually exclusive with excludedAttributes. Example: userName,emails.value
- `excludedAttributes` (query, string, optional) — Resource attributes to be excluded from response. Mutually exclusive with attributes. Example: timezone,emails.type,department

## Original description

Retrieves a user from the directory based on their `userId`.
