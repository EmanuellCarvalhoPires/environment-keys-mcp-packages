---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/blog-post
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_blog_post_by_id
title: "Confluence v2 - Get blog post by id"
kind: request
request: "[[Confluence v2 - Get blog post by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /blogposts/{id} · Get blog post by id. Returns a specific blog post. Permissions required: Permission to view the blog post and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the blog post to be returned. If you don't know the blog post ID, use Get blog posts and filter the results."
  "body_format":
    type: string
    required: false
    description: "The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
  "get_draft":
    type: string
    required: false
    description: "Retrieve the draft version of this blog post."
  "status":
    type: string
    required: false
    description: "Filter the blog post being retrieved by its status."
  "version":
    type: string
    required: false
    description: "Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details."
  "include_labels":
    type: string
    required: false
    description: "Includes labels associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_properties":
    type: string
    required: false
    description: "Includes content properties associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_operations":
    type: string
    required: false
    description: "Includes operations associated with this blog post in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order."
  "include_likes":
    type: string
    required: false
    description: "Includes likes associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_versions":
    type: string
    required: false
    description: "Includes versions associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_version":
    type: string
    required: false
    description: "Includes the current version associated with this blog post in the response. By default this is included and can be omitted by setting the value to false."
  "include_favorited_by_current_user_status":
    type: string
    required: false
    description: "Includes whether this blog post has been favorited by the current user."
  "include_webresources":
    type: string
    required: false
    description: "Includes web resources that can be used to render blog post content on a client."
  "include_collaborators":
    type: string
    required: false
    description: "Includes collaborators on the blog post."
writes: false
expose: false
---
# confluence_get_blog_post_by_id

`GET /blogposts/{id}` — Get blog post by id

- Request: [[Confluence v2 - Get blog post by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
