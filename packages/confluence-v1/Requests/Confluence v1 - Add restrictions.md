---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/content/{id}/restriction"
category: "Content restrictions"
writes_data: true
tool_note: "[[confluence_v1_add_restrictions]]"
---
# Confluence v1 - Add restrictions

**Add restrictions** — `POST /wiki/rest/api/content/{id}/restriction`

- Run by the tool [[confluence_v1_add_restrictions]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the content to add restrictions to.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content restrictions (returned in response) to expand.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds restrictions to a piece of content. Note, this does not change any
existing restrictions on the content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the content.
