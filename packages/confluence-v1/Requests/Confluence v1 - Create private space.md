---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/space/_private"
category: "Space"
writes_data: true
tool_note: "[[confluence_v1_create_private_space]]"
---
# Confluence v1 - Create private space

**Create private space** — `POST /wiki/rest/api/space/_private`

- Run by the tool [[confluence_v1_create_private_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/space/_private
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new space that is only visible to the creator. This method is
the same as the [Create space](#api-space-post) method with permissions
set to the current user only. Note, currently you cannot set space
labels when creating a space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Create Space(s)' global permission.
