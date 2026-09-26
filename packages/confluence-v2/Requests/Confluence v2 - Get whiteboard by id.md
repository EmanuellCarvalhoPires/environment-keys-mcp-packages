---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/whiteboard
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/whiteboards/{id}"
category: "Whiteboard"
writes_data: false
tool_note: "[[confluence_get_whiteboard_by_id]]"
---
# Confluence v2 - Get whiteboard by id

**Get whiteboard by id** — `GET /whiteboards/{id}`

- Run by the tool [[confluence_get_whiteboard_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/whiteboards/{{param:id}}?include-collaborators={{param:include_collaborators}}&include-direct-children={{param:include_direct_children}}&include-operations={{param:include_operations}}&include-properties={{param:include_properties}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the whiteboard to be returned
- `include_collaborators` (query, string, optional) — Includes collaborators on the whiteboard.
- `include_direct_children` (query, string, optional) — Includes direct children of the whiteboard, as defined in the ChildrenResponse object.
- `include_operations` (query, string, optional) — Includes operations associated with this whiteboard in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order.
- `include_properties` (query, string, optional) — Includes content properties associated with this whiteboard in the response. The number of results will be limited to 50 and sorted in the default sort order.

## Original description

Returns a specific whiteboard.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the whiteboard and its corresponding space.
