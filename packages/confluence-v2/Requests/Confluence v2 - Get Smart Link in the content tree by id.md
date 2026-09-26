---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/smart-link
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/embeds/{id}"
category: "Smart Link"
writes_data: false
tool_note: "[[confluence_get_smart_link_in_the_content_tree_by_id]]"
---
# Confluence v2 - Get Smart Link in the content tree by id

**Get Smart Link in the content tree by id** — `GET /embeds/{id}`

- Run by the tool [[confluence_get_smart_link_in_the_content_tree_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/embeds/{{param:id}}?include-collaborators={{param:include_collaborators}}&include-direct-children={{param:include_direct_children}}&include-operations={{param:include_operations}}&include-properties={{param:include_properties}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the Smart Link in the content tree to be returned.
- `include_collaborators` (query, string, optional) — Includes collaborators on the Smart Link.
- `include_direct_children` (query, string, optional) — Includes direct children of the Smart Link, as defined in the ChildrenResponse object.
- `include_operations` (query, string, optional) — Includes operations associated with this Smart Link in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order.
- `include_properties` (query, string, optional) — Includes content properties associated with this Smart Link in the response. The number of results will be limited to 50 and sorted in the default sort order.

## Original description

Returns a specific Smart Link in the content tree.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the Smart Link in the content tree and its corresponding space.
