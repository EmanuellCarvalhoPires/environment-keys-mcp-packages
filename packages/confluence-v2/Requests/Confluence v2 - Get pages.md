---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/page
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/pages"
category: "Page"
writes_data: false
tool_note: "[[confluence_get_pages]]"
---
# Confluence v2 - Get pages

**Get pages** — `GET /pages`

- Run by the tool [[confluence_get_pages]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/pages?id={{param:id}}&space-id={{param:space_id}}&sort={{param:sort}}&status={{param:status}}&title={{param:title}}&body-format={{param:body_format}}&subtype={{param:subtype}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (query, string, optional) — Filter the results based on page ids. Multiple page ids can be specified as a comma-separated list.
- `space_id` (query, string, optional) — Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.
- `sort` (query, string, optional) — Used to sort the result by a particular field.
- `status` (query, string, optional) — Filter the results to pages based on their status. By default, current and archived are used.
- `title` (query, string, optional) — Filter the results to pages based on their title.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `subtype` (query, string, optional) — Filter the results to pages based on their subtype.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of pages per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.

## Original description

Returns all pages. The number of results is limited by the `limit` parameter and additional results (if available)
will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
Only pages that the user has permission to view will be returned.
