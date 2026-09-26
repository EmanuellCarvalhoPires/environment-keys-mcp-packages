---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/users-bulk"
category: "User"
writes_data: true
tool_note: "[[confluence_create_bulk_user_lookup_using_ids]]"
---
# Confluence v2 - Create bulk user lookup using ids

**Create bulk user lookup using ids** — `POST /users-bulk`

- Run by the tool [[confluence_create_bulk_user_lookup_using_ids]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/users-bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Returns user details for the ids provided in the request body.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
The user must be able to view user profiles in the Confluence site.
