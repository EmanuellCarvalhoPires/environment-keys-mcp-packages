---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_comment_attachments
title: "JSM - Get comment attachments"
kind: request
request: "[[JSM - Get comment attachments]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/comment/{commentId}/attachment · Get comment attachments. This method returns the attachments referenced in a comment. Permissions required: Permission to view the customer request. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request that contains the comment."
  "commentId":
    type: string
    required: true
    description: "The ID of the comment."
  "start":
    type: string
    required: false
    description: "The starting index of the returned comments. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of comments to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: false
---
# jsm_get_comment_attachments

`GET /rest/servicedeskapi/request/{issueIdOrKey}/comment/{commentId}/attachment` — Get comment attachments

- Request: [[JSM - Get comment attachments]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
