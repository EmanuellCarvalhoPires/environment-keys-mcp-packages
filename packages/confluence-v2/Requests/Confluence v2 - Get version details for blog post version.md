---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/version
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/blogposts/{blogpost-id}/versions/{version-number}"
category: "Version"
writes_data: false
tool_note: "[[confluence_get_version_details_for_blog_post_version]]"
---
# Confluence v2 - Get version details for blog post version

**Get version details for blog post version** — `GET /blogposts/{blogpost-id}/versions/{version-number}`

- Run by the tool [[confluence_get_version_details_for_blog_post_version]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/blogposts/{{param:blogpost_id}}/versions/{{param:version_number}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `blogpost_id` (path, string, required) — The ID of the blog post for which version details should be returned.
- `version_number` (path, string, required) — The version number of the blog post to be returned.

## Original description

Retrieves version details for the specified blog post and version number.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the blog post.
