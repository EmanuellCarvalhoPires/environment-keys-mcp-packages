---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/whiteboards/{id}/properties"
category: "Content Properties"
writes_data: false
tool_note: "[[confluence_get_content_properties_for_whiteboard]]"
---
# Confluence v2 - Get content properties for whiteboard

**Get content properties for whiteboard** — `GET /whiteboards/{id}/properties`

- Run by the tool [[confluence_get_content_properties_for_whiteboard]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/whiteboards/{{param:id}}/properties?key={{param:key}}&sort={{param:sort}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the whiteboard for which content properties should be returned.
- `key` (query, string, optional) — Filters the response to return a specific content property with matching key (case sensitive).
- `sort` (query, string, optional) — Used to sort the result by a particular field.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of attachments per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.

## Original description

Retrieves Content Properties tied to a specified whiteboard.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the whiteboard.
