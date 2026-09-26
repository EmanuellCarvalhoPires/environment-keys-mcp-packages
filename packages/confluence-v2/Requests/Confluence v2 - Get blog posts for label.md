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
path: "/labels/{id}/blogposts"
category: "Blog Post"
writes_data: false
tool_note: "[[confluence_get_blog_posts_for_label]]"
---
# Confluence v2 - Get blog posts for label

**Get blog posts for label** — `GET /labels/{id}/blogposts`

- Run by the tool [[confluence_get_blog_posts_for_label]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/labels/{{param:id}}/blogposts?space-id={{param:space_id}}&body-format={{param:body_format}}&sort={{param:sort}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the label for which blog posts should be returned.
- `space_id` (query, string, optional) — Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `sort` (query, string, optional) — Used to sort the result by a particular field.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of blog posts per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.

## Original description

Returns the blogposts of specified label. The number of results is limited by the `limit` parameter and additional results (if available)
will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page and its corresponding space.
