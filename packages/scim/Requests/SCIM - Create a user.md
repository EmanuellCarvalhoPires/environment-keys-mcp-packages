---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/users
  - api/operation/create
  - api/effect/write
up: "[[MCP - SCIM]]"
app: "SCIM"
method: POST
path: "/scim/directory/{directoryId}/Users"
category: "Users"
writes_data: true
---
# SCIM - Create a user

**Create a user** — `POST /scim/directory/{directoryId}/Users`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"SCIM - Create a user"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
POST https://api.atlassian.com/scim/directory/{{param:directoryId}}/Users?attributes={{param:attributes}}&excludedAttributes={{param:excludedAttributes}}
Authorization: {{service.scim_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `attributes` (query, string, optional) — Resource attributes to be included in response. Mutually exclusive from excludedAttributes. Example: userName,emails.value
- `excludedAttributes` (query, string, optional) — Resource attributes to be excluded from response. Mutually exclusive from attributes. Example: timezone,emails.type,department
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a user in the directory.
**Note:** An attempt to create an existing user will fail with a 409 (Conflict) error.

Use this API to manage accounts outside your organization when assigning these users to SCIM groups.

If there's already a managed Atlassian account associated with the specified email address on the Atlassian platform, the user in your identity provider will be connected or linked to the user in your Atlassian organization.
