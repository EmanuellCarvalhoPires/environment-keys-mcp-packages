---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/children
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/pages/{id}/children"
category: "Children"
writes_data: false
tool_note: "[[confluence_get_child_pages]]"
---
# Confluence v2 - Get child pages

**Get child pages** — `GET /pages/{id}/children`

- Run by the tool [[confluence_get_child_pages]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/pages/{{param:id}}/children?cursor={{param:cursor}}&limit={{param:limit}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the parent page. If you don't know the page ID, use Get pages and filter the results.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of pages per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.
- `sort` (query, string, optional) — Used to sort the result by a particular field.

## Original description

Returns all child pages for given page id. The number of results is limited by the `limit` parameter and additional results (if available)
will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
Only pages that the user has permission to view will be returned.
