---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/users
  - api/operation/update
  - api/effect/write
up: "[[MCP - SCIM]]"
app: "SCIM"
method: PATCH
path: "/scim/directory/{directoryId}/Users/{userId}"
category: "Users"
writes_data: true
---
# SCIM - Update user by ID (PATCH)

**Update user by ID (PATCH)** — `PATCH /scim/directory/{directoryId}/Users/{userId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"SCIM - Update user by ID (PATCH)"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
PATCH https://api.atlassian.com/scim/directory/{{param:directoryId}}/Users/{{param:userId}}?attributes={{param:attributes}}&excludedAttributes={{param:excludedAttributes}}
Authorization: {{service.scim_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `userId` (path, string, required) — Unique ID to identiy the users. Use the Get users API to get the userId.
- `attributes` (query, string, optional) — Resource attributes to be included in the response. Mutually exclusive from excludedAttributes. Example: userName,emails.value
- `excludedAttributes` (query, string, optional) — Resource attributes to be included in the response. Mutually exclusive from attributes. Example: timezone,emails.type,department
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates a user's information in the directory based on their `userId` via `PATCH`. Refer to  [Service Provider Configuration APIs](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-service-provider-configuration/#api-group-service-provider-configuration) for details on supported operations.
