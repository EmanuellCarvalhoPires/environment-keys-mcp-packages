---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_inline_comment_by_id
title: "Confluence v2 - Get inline comment by id"
kind: request
request: "[[Confluence v2 - Get inline comment by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /inline-comments/{comment-id} · Get inline comment by id. Retrieves an inline comment by id Permissions required: Permission to view the content of the page or blogpost and its corresponding space. Writes data: no."
params:
  "comment_id":
    type: string
    required: true
    description: "The ID of the comment to be retrieved."
  "body_format":
    type: string
    required: false
    description: "The content format type to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
  "version":
    type: string
    required: false
    description: "Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details."
  "include_properties":
    type: string
    required: false
    description: "Includes content properties associated with this inline comment in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_operations":
    type: string
    required: false
    description: "Includes operations associated with this inline comment in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order."
  "include_likes":
    type: string
    required: false
    description: "Includes likes associated with this inline comment in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_versions":
    type: string
    required: false
    description: "Includes versions associated with this inline comment in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_version":
    type: string
    required: false
    description: "Includes the current version associated with this inline comment in the response. By default this is included and can be omitted by setting the value to false."
writes: false
expose: false
---
# confluence_get_inline_comment_by_id

`GET /inline-comments/{comment-id}` — Get inline comment by id

- Request: [[Confluence v2 - Get inline comment by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
