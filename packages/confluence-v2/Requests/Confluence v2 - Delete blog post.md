---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/blog-post
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/blogposts/{id}"
category: "Blog Post"
writes_data: true
tool_note: "[[confluence_delete_blog_post]]"
---
# Confluence v2 - Delete blog post

**Delete blog post** — `DELETE /blogposts/{id}`

- Run by the tool [[confluence_delete_blog_post]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/blogposts/{{param:id}}?purge={{param:purge}}&draft={{param:draft}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the blog post to be deleted.
- `purge` (query, string, optional) — If attempting to purge the blog post.
- `draft` (query, string, optional) — If attempting to delete a blog post that is a draft.

## Original description

Delete a blog post by id.

By default this will delete blog posts that are non-drafts. To delete a blog post that is a draft, the endpoint must be called on a 
draft with the following param `draft=true`. Discarded drafts are not sent to the trash and are permanently deleted.

Deleting a blog post that is not a draft moves the blog post to the trash, where it can be restored later.
To permanently delete a blog post (or "purge" it), the endpoint must be called on a **trashed** blog post with the following param `purge=true`.

**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
Permission to view the blog post and its corresponding space.
Permission to delete blog posts in the space.
[`manage/content`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space (if attempting to purge).

**Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
