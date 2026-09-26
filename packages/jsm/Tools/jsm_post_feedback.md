---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_post_feedback
title: "JSM - Post feedback"
kind: request
request: "[[JSM - Post feedback]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/request/{requestIdOrKey}/feedback · Post feedback. This method adds a feedback on an request using it's requestKey or requestId Permissions required: User must be the reporter or an Atlassian Connect app. Writes data: yes."
params:
  "requestIdOrKey":
    type: string
    required: true
    description: "The id or the key of the request to post the feedback on"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_post_feedback

`POST /rest/servicedeskapi/request/{requestIdOrKey}/feedback` — Post feedback

- Request: [[JSM - Post feedback]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
