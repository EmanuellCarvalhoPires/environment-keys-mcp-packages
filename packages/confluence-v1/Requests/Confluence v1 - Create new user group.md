---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/group
  - api/operation/create
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/group"
category: "Group"
writes_data: true
tool_note: "[[confluence_v1_create_new_user_group]]"
---
# Confluence v1 - Create new user group

**Create new user group** — `POST /wiki/rest/api/group`

- Run by the tool [[confluence_v1_create_new_user_group]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/group
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new user group.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be a site admin.
