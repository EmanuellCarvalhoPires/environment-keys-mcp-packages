---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/pages/{id}/inline-comments"
category: "Comment"
writes_data: false
tool_note: "[[confluence_get_inline_comments_for_page]]"
---
# Confluence v2 - Get inline comments for page

**Get inline comments for page** — `GET /pages/{id}/inline-comments`

- Run by the tool [[confluence_get_inline_comments_for_page]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/pages/{{param:id}}/inline-comments?body-format={{param:body_format}}&status={{param:status}}&resolution-status={{param:resolution_status}}&sort={{param:sort}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the page for which inline comments should be returned.
- `body_format` (query, string, optional) — The content format type to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `status` (query, string, optional) — Filter the inline comment being retrieved by its status.
- `resolution_status` (query, string, optional) — Filter the inline comment being retrieved by its resolution status.
- `sort` (query, string, optional) — Used to sort the result by a particular field.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of inline comments per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.

## Original description

Returns the root inline comments of specific page. The number of results is limited by the `limit` parameter and additional results (if available)
will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page and its corresponding space.
