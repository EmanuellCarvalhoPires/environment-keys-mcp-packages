---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/spaces/{id}"
category: "Space"
writes_data: false
tool_note: "[[confluence_get_space_by_id]]"
---
# Confluence v2 - Get space by id

**Get space by id** — `GET /spaces/{id}`

- Run by the tool [[confluence_get_space_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/spaces/{{param:id}}?description-format={{param:description_format}}&include-icon={{param:include_icon}}&include-operations={{param:include_operations}}&include-properties={{param:include_properties}}&include-permissions={{param:include_permissions}}&include-role-assignments={{param:include_role_assignments}}&include-labels={{param:include_labels}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the space to be returned.
- `description_format` (query, string, optional) — The content format type to be returned in the description field of the response. If available, the representation will be available under a response field of the same name under the description field.
- `include_icon` (query, string, optional) — If the icon for the space should be fetched or not.
- `include_operations` (query, string, optional) — Includes operations associated with this space in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order.
- `include_properties` (query, string, optional) — Includes space properties associated with this space in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_permissions` (query, string, optional) — Includes space permissions associated with this space in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_role_assignments` (query, string, optional) — Includes role assignments associated with this space in the response. This parameter is only accepted for EAP sites. The number of results will be limited to 50 and sorted in the default sort order.
- `include_labels` (query, string, optional) — Includes labels associated with this space in the response. The number of results will be limited to 50 and sorted in the default sort order.

## Original description

Returns a specific space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the space.
