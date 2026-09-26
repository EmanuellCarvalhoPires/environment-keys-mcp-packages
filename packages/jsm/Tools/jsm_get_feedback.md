---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_feedback
title: "JSM - Get feedback"
kind: request
request: "[[JSM - Get feedback]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{requestIdOrKey}/feedback · Get feedback. This method retrieves a feedback of a request using it's requestKey or requestId Permissions required: User has view request permissions. Writes data: no."
params:
  "requestIdOrKey":
    type: string
    required: true
    description: "The id or the key of the request to post the feedback on"
writes: false
expose: false
---
# jsm_get_feedback

`GET /rest/servicedeskapi/request/{requestIdOrKey}/feedback` — Get feedback

- Request: [[JSM - Get feedback]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
