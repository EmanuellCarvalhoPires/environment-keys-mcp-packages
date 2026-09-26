---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_create_request_comment
title: "JSM - Create request comment"
kind: request
request: "[[JSM - Create request comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/request/{issueIdOrKey}/comment · Create request comment. This method creates a public or private (internal) comment on a customer request, with the comment visibility set by public. The user recorded as the author of the comment. Permissions required: User has Add Comments permission. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to which the comment will be added."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_create_request_comment

`POST /rest/servicedeskapi/request/{issueIdOrKey}/comment` — Create request comment

- Request: [[JSM - Create request comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
