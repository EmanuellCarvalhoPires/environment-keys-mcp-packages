---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/descendants
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/databases/{id}/descendants"
category: "Descendants"
writes_data: false
tool_note: "[[confluence_get_descendants_of_a_database]]"
---
# Confluence v2 - Get descendants of a database

**Get descendants of a database** — `GET /databases/{id}/descendants`

- Run by the tool [[confluence_get_descendants_of_a_database]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/databases/{{param:id}}/descendants?limit={{param:limit}}&depth={{param:depth}}&cursor={{param:cursor}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the database.
- `limit` (query, string, optional) — Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results.
- `depth` (query, string, optional) — Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.

## Original description

Returns descendants in the content tree for a given database by ID in top-to-bottom order (that is, the highest descendant is the first
item in the response payload). The number of results is limited by the `limit` parameter and additional results (if available)
will be available by calling this endpoint with the cursor in the response payload. There is also a `depth` parameter specifying depth
of descendants to be fetched.

The following types of content will be returned:
- Database
- Embed
- Folder
- Page
- Whiteboard

This endpoint returns minimal information about each descendant. To fetch more details, use a related endpoint based on the content type, such
as:

- [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
- [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
- [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
- [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
- [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
Permission to view the database and its corresponding space
