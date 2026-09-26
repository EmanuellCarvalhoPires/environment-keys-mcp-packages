---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/blog-post
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_blog_post
title: "Confluence v2 - Delete blog post"
kind: request
request: "[[Confluence v2 - Delete blog post]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /blogposts/{id} · Delete blog post. Delete a blog post by id. By default this will delete blog posts that are non-drafts. To delete a blog post that is a draft, the endpoint must be called on a draft with the following param draft=true. Discarded drafts are not sent to the trash and are permanently deleted. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the blog post to be deleted."
  "purge":
    type: string
    required: false
    description: "If attempting to purge the blog post."
  "draft":
    type: string
    required: false
    description: "If attempting to delete a blog post that is a draft."
writes: true
expose: false
---
# confluence_delete_blog_post

`DELETE /blogposts/{id}` — Delete blog post

- Request: [[Confluence v2 - Delete blog post]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
