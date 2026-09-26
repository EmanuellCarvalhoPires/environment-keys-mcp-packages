---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/content/{id}/restriction"
category: "Content restrictions"
writes_data: true
tool_note: "[[confluence_v1_update_restrictions]]"
---
# Confluence v1 - Update restrictions

**Update restrictions** — `PUT /wiki/rest/api/content/{id}/restriction`

- Run by the tool [[confluence_v1_update_restrictions]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the content to update restrictions for.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content restrictions (returned in response) to expand.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates restrictions for a piece of content. This removes the existing
restrictions and replaces them with the restrictions in the request.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the content.
