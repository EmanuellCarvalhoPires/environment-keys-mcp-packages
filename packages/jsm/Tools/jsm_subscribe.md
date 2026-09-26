---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_subscribe
title: "JSM - Subscribe"
kind: request
request: "[[JSM - Subscribe]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · PUT /rest/servicedeskapi/request/{issueIdOrKey}/notification · Subscribe. This method subscribes the user to receiving notifications from a customer request. Permissions required: Permission to view the customer request. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to be subscribed to."
writes: true
expose: false
---
# jsm_subscribe

`PUT /rest/servicedeskapi/request/{issueIdOrKey}/notification` — Subscribe

- Request: [[JSM - Subscribe]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
