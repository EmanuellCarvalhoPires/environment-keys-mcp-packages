---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/custom-content
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/spaces/{id}/custom-content"
category: "Custom Content"
writes_data: false
tool_note: "[[confluence_get_custom_content_by_type_in_space]]"
---
# Confluence v2 - Get custom content by type in space

**Get custom content by type in space** — `GET /spaces/{id}/custom-content`

- Run by the tool [[confluence_get_custom_content_by_type_in_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/spaces/{{param:id}}/custom-content?type={{param:type}}&cursor={{param:cursor}}&limit={{param:limit}}&body-format={{param:body_format}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the space for which custom content should be returned.
- `type` (query, string, required) — The type of custom content being requested. See: https://developer.atlassian.com/cloud/confluence/custom-content/ for additional details on custom content.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of pages per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.

## Original description

Returns all custom content for a given type within a given space. The number of results is limited by the `limit` parameter and additional results (if available)
will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the custom content and the corresponding space.
