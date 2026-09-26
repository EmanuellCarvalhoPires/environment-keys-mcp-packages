---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/blog-post
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/blogposts/{id}"
category: "Blog Post"
writes_data: true
tool_note: "[[confluence_update_blog_post]]"
---
# Confluence v2 - Update blog post

**Update blog post** — `PUT /blogposts/{id}`

- Run by the tool [[confluence_update_blog_post]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/blogposts/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the blog post to be updated. If you don't know the blog post ID, use Get Blog Posts and filter the results.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a blog post by id.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the blog post and its corresponding space. Permission to update blog posts in the space.
