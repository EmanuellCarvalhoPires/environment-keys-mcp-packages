---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/version
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/pages/{id}/versions"
category: "Version"
writes_data: false
tool_note: "[[confluence_get_page_versions]]"
---
# Confluence v2 - Get page versions

**Get page versions** — `GET /pages/{id}/versions`

- Run by the tool [[confluence_get_page_versions]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/pages/{{param:id}}/versions?body-format={{param:body_format}}&cursor={{param:cursor}}&limit={{param:limit}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the page to be queried for its versions. If you don't know the page ID, use Get pages and filter the results.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of versions per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.
- `sort` (query, string, optional) — Used to sort the result by a particular field.

## Original description

Returns the versions of specific page.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the page and its corresponding space.
