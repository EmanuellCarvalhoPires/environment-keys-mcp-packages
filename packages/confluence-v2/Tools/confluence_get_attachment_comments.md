---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_attachment_comments
title: "Confluence v2 - Get attachment comments"
kind: request
request: "[[Confluence v2 - Get attachment comments]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /attachments/{id}/footer-comments · Get attachment comments. Returns the comments of the specific attachment. The number of results is limited by the limit parameter and additional results (if available) will be available through the next URL present in the Link response header. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment for which comments should be returned."
  "body_format":
    type: string
    required: false
    description: "The content format type to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of comments per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
  "sort":
    type: string
    required: false
    description: "Used to sort the result by a particular field."
  "version":
    type: string
    required: false
    description: "Version number of the attachment to retrieve comments for. If no version provided, retrieves comments for the latest version."
writes: false
expose: false
---
# confluence_get_attachment_comments

`GET /attachments/{id}/footer-comments` — Get attachment comments

- Request: [[Confluence v2 - Get attachment comments]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
