---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/blogposts/{id}/classification-level"
category: "Classification Level"
writes_data: false
tool_note: "[[confluence_get_blog_post_classification_level]]"
---
# Confluence v2 - Get blog post classification level

**Get blog post classification level** — `GET /blogposts/{id}/classification-level`

- Run by the tool [[confluence_get_blog_post_classification_level]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/blogposts/{{param:id}}/classification-level?status={{param:status}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the blog post for which classification level should be returned.
- `status` (query, string, optional) — Status of blog post from which classification level will fetched.

## Original description

Returns the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
for a specific blog post.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Permission to access the Confluence site ('Can use' global permission) and permission to view the blog post.
'Permission to edit the blog post is required if trying to view classification level for a draft.
