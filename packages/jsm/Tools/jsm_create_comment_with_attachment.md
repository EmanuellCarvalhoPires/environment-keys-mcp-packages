---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_create_comment_with_attachment
title: "JSM - Create comment with attachment"
kind: request
request: "[[JSM - Create comment with attachment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/request/{issueIdOrKey}/attachment · Create comment with attachment. This method creates a comment on a customer request using one or more attachment files (uploaded using servicedeskapi/servicedesk/\\{serviceDeskId\\}/attachTemporaryFile), with the visibility set by public. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to which the attachment will be added."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_create_comment_with_attachment

`POST /rest/servicedeskapi/request/{issueIdOrKey}/attachment` — Create comment with attachment

- Request: [[JSM - Create comment with attachment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
