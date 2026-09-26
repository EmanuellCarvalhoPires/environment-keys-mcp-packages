---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_unsubscribe
title: "JSM - Unsubscribe"
kind: request
request: "[[JSM - Unsubscribe]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · DELETE /rest/servicedeskapi/request/{issueIdOrKey}/notification · Unsubscribe. This method unsubscribes the user from notifications from a customer request. Permissions required: Permission to view the customer request. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to be unsubscribed from."
writes: true
expose: false
---
# jsm_unsubscribe

`DELETE /rest/servicedeskapi/request/{issueIdOrKey}/notification` — Unsubscribe

- Request: [[JSM - Unsubscribe]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
