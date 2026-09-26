---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/content/{id}/restriction/byOperation"
category: "Content restrictions"
writes_data: false
tool_note: "[[confluence_v1_get_restrictions_by_operation]]"
---
# Confluence v1 - Get restrictions by operation

**Get restrictions by operation** — `GET /wiki/rest/api/content/{id}/restriction/byOperation`

- Run by the tool [[confluence_v1_get_restrictions_by_operation]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction/byOperation?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the content to be queried for its restrictions.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content restrictions to expand. - restrictions.user returns the piece of content that the restrictions are applied to. Expanded by default.

## Original description

Returns restrictions on a piece of content by operation. This method is
similar to [Get restrictions](#api-content-id-restriction-get) except that
the operations are properties of the return object, rather than items in
a results array.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content.
