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
method: PUT
path: "/scim/directory/{directoryId}/Users/{userId}"
category: "Users"
writes_data: true
---
# SCIM - Update user via user attributes

**Update user via user attributes** — `PUT /scim/directory/{directoryId}/Users/{userId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"SCIM - Update user via user attributes"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
PUT https://api.atlassian.com/scim/directory/{{param:directoryId}}/Users/{{param:userId}}?attributes={{param:attributes}}&excludedAttributes={{param:excludedAttributes}}
Authorization: {{service.scim_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `userId` (path, string, required) — Unique ID to identiy the users. Use the Get users API to get the userId.
- `attributes` (query, string, optional) — Resource attributes to be included in the response. Mutually exclusive from excludedAttributes. Example: userName,emails.value
- `excludedAttributes` (query, string, optional) — Resource attributes to be excluded in the response. Mutually exclusive from attributes. Example: timezone,emails.type,department
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update the directory-based user information using the user attributes associated with their `userId`. User information  is replaced attribute-by-attribute, with the exception of immutable and read-only  attributes. Existing values of unspecified attributes are cleaned.
