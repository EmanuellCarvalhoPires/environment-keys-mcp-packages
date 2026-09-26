---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/smart-link
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/embeds"
category: "Smart Link"
writes_data: true
tool_note: "[[confluence_create_smart_link_in_the_content_tree]]"
---
# Confluence v2 - Create Smart Link in the content tree

**Create Smart Link in the content tree** — `POST /embeds`

- Run by the tool [[confluence_create_smart_link_in_the_content_tree]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/embeds
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a Smart Link in the content tree in the space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the corresponding space. Permission to create a Smart Link in the content tree in the space.
