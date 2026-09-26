---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/blog-post
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/blogposts/{id}"
category: "Blog Post"
writes_data: false
tool_note: "[[confluence_get_blog_post_by_id]]"
---
# Confluence v2 - Get blog post by id

**Get blog post by id** — `GET /blogposts/{id}`

- Run by the tool [[confluence_get_blog_post_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/blogposts/{{param:id}}?body-format={{param:body_format}}&get-draft={{param:get_draft}}&status={{param:status}}&version={{param:version}}&include-labels={{param:include_labels}}&include-properties={{param:include_properties}}&include-operations={{param:include_operations}}&include-likes={{param:include_likes}}&include-versions={{param:include_versions}}&include-version={{param:include_version}}&include-favorited-by-current-user-status={{param:include_favorited_by_current_user_status}}&include-webresources={{param:include_webresources}}&include-collaborators={{param:include_collaborators}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the blog post to be returned. If you don't know the blog post ID, use Get blog posts and filter the results.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `get_draft` (query, string, optional) — Retrieve the draft version of this blog post.
- `status` (query, string, optional) — Filter the blog post being retrieved by its status.
- `version` (query, string, optional) — Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
- `include_labels` (query, string, optional) — Includes labels associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_properties` (query, string, optional) — Includes content properties associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_operations` (query, string, optional) — Includes operations associated with this blog post in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order.
- `include_likes` (query, string, optional) — Includes likes associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_versions` (query, string, optional) — Includes versions associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_version` (query, string, optional) — Includes the current version associated with this blog post in the response. By default this is included and can be omitted by setting the value to false.
- `include_favorited_by_current_user_status` (query, string, optional) — Includes whether this blog post has been favorited by the current user.
- `include_webresources` (query, string, optional) — Includes web resources that can be used to render blog post content on a client.
- `include_collaborators` (query, string, optional) — Includes collaborators on the blog post.

## Original description

Returns a specific blog post.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the blog post and its corresponding space.
