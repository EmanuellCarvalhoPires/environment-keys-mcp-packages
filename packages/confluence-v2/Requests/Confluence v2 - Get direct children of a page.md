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
path: "/pages/{id}/direct-children"
category: "Children"
writes_data: false
tool_note: "[[confluence_get_direct_children_of_a_page]]"
---
# Confluence v2 - Get direct children of a page

**Get direct children of a page** — `GET /pages/{id}/direct-children`

- Run by the tool [[confluence_get_direct_children_of_a_page]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/pages/{{param:id}}/direct-children?cursor={{param:cursor}}&limit={{param:limit}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the parent page.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of items per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.
- `sort` (query, string, optional) — Used to sort the result by a particular field.

## Original description

Returns all children for given page id in the content tree. The number of results is limited by the `limit` parameter and additional results (if available)
will be available through the `next` URL present in the `Link` response header.

The following types of content will be returned:
- Database
- Embed
- Folder
- Page
- Whiteboard

This endpoint returns minimal information about each child. To fetch more details, use a related endpoint based on the content type, such
as:

- [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
- [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
- [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
- [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
- [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
Only content that the user has permission to view will be returned.
