---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/ancestors
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/folders/{id}/ancestors"
category: "Ancestors"
writes_data: false
tool_note: "[[confluence_get_all_ancestors_of_folder]]"
---
# Confluence v2 - Get all ancestors of folder

**Get all ancestors of folder** — `GET /folders/{id}/ancestors`

- Run by the tool [[confluence_get_all_ancestors_of_folder]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/folders/{{param:id}}/ancestors?limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the folder.
- `limit` (query, string, optional) — Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results.

## Original description

Returns all ancestors for a given folder by ID in top-to-bottom order (that is, the highest ancestor is
the first item in the response payload). The number of results is limited by the `limit` parameter and additional results 
(if available) will be available by calling this endpoint with the ID of first ancestor in the response payload.

This endpoint returns minimal information about each ancestor. To fetch more details, use a related endpoint, such
as [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-folders-id-get).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
Permission to view the folder and its corresponding space
