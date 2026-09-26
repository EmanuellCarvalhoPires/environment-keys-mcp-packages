---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/blog-post
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/blogposts"
category: "Blog Post"
writes_data: true
tool_note: "[[confluence_create_blog_post]]"
---
# Confluence v2 - Create blog post

**Create blog post** — `POST /blogposts`

- Run by the tool [[confluence_create_blog_post]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/blogposts?private={{param:private}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `private` (query, string, optional) — The blog post will be private. Only the user who creates this blog post will have permission to view and edit one.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new blog post in the space specified by the spaceId.

By default this will create the blog post as a non-draft, unless the status is specified as draft.
If creating a non-draft, the title must not be empty.

Currently only supports the storage representation specified in the body.representation enums below
