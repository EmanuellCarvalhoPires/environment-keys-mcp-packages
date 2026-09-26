---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_remove_request_participants
title: "JSM - Remove request participants"
kind: request
request: "[[JSM - Remove request participants]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · DELETE /rest/servicedeskapi/request/{issueIdOrKey}/participant · Remove request participants. This method removes participants from a customer request. Permissions required: Permission to manage participants on the customer request. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to have participants removed."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_remove_request_participants

`DELETE /rest/servicedeskapi/request/{issueIdOrKey}/participant` — Remove request participants

- Request: [[JSM - Remove request participants]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
