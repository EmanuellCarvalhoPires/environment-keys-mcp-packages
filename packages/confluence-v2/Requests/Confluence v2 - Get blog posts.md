---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/blog-post
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/blogposts"
category: "Blog Post"
writes_data: false
tool_note: "[[confluence_get_blog_posts]]"
---
# Confluence v2 - Get blog posts

**Get blog posts** — `GET /blogposts`

- Run by the tool [[confluence_get_blog_posts]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/blogposts?id={{param:id}}&space-id={{param:space_id}}&sort={{param:sort}}&status={{param:status}}&title={{param:title}}&body-format={{param:body_format}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (query, string, optional) — Filter the results based on blog post ids. Multiple blog post ids can be specified as a comma-separated list.
- `space_id` (query, string, optional) — Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.
- `sort` (query, string, optional) — Used to sort the result by a particular field.
- `status` (query, string, optional) — Filter the results to blog posts based on their status. By default, current is used.
- `title` (query, string, optional) — Filter the results to blog posts based on their title.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of blog posts per result to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results.

## Original description

Returns all blog posts. The number of results is limited by the `limit` parameter and additional results (if available)
will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
Only blog posts that the user has permission to view will be returned.
