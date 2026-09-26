---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_perform_customer_transition
title: "JSM - Perform customer transition"
kind: request
request: "[[JSM - Perform customer transition]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/request/{issueIdOrKey}/transition · Perform customer transition. This method performs a customer transition for a given request and transition. An optional comment can be included to provide a reason for the transition. Permissions required: The user must be able to view the request and have the Transition Issues permission. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "ID or key of the issue to transition"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_perform_customer_transition

`POST /rest/servicedeskapi/request/{issueIdOrKey}/transition` — Perform customer transition

- Request: [[JSM - Perform customer transition]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
