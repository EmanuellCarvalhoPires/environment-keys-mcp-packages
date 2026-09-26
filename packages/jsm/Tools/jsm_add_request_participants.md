---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_add_request_participants
title: "JSM - Add request participants"
kind: request
request: "[[JSM - Add request participants]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/request/{issueIdOrKey}/participant · Add request participants. This method adds participants to a customer request. Permissions required: Permission to manage participants on the customer request. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to have participants added."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_add_request_participants

`POST /rest/servicedeskapi/request/{issueIdOrKey}/participant` — Add request participants

- Request: [[JSM - Add request participants]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
