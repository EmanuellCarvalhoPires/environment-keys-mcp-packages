---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_subscription_status
title: "JSM - Get subscription status"
kind: request
request: "[[JSM - Get subscription status]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/notification · Get subscription status. This method returns the notification subscription status of the user making the request. Use this method to determine if the user is subscribed to a customer request's notifications. Permissions required: Permission to view the customer request. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to be queried for subscription status."
writes: false
expose: false
---
# jsm_get_subscription_status

`GET /rest/servicedeskapi/request/{issueIdOrKey}/notification` — Get subscription status

- Request: [[JSM - Get subscription status]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
