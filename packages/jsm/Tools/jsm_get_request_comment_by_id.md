---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_request_comment_by_id
title: "JSM - Get request comment by id"
kind: request
request: "[[JSM - Get request comment by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/comment/{commentId} · Get request comment by id. This method returns details of a customer request's comment. Permissions required: Permission to view the customer request. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request that contains the comment."
  "commentId":
    type: string
    required: true
    description: "The ID of the comment to retrieve."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the comment to expand: attachment returns the attachment details, if any, for the comment."
writes: false
expose: false
---
# jsm_get_request_comment_by_id

`GET /rest/servicedeskapi/request/{issueIdOrKey}/comment/{commentId}` — Get request comment by id

- Request: [[JSM - Get request comment by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
