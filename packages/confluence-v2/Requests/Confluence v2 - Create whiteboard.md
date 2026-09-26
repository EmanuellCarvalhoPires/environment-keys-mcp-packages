---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/whiteboard
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/whiteboards"
category: "Whiteboard"
writes_data: true
tool_note: "[[confluence_create_whiteboard]]"
---
# Confluence v2 - Create whiteboard

**Create whiteboard** — `POST /whiteboards`

- Run by the tool [[confluence_create_whiteboard]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/whiteboards?private={{param:private}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `private` (query, string, optional) — The whiteboard will be private. Only the user who creates this whiteboard will have permission to view and edit one.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a whiteboard in the space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the corresponding space. Permission to create a whiteboard in the space.
