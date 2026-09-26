---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_delete_feedback
title: "JSM - Delete feedback"
kind: request
request: "[[JSM - Delete feedback]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · DELETE /rest/servicedeskapi/request/{requestIdOrKey}/feedback · Delete feedback. This method deletes the feedback of request using it's requestKey or requestId Permissions required: User must be the reporter or an Atlassian Connect app. Writes data: yes."
params:
  "requestIdOrKey":
    type: string
    required: true
    description: "The id or the key of the request to post the feedback on"
writes: true
expose: false
---
# jsm_delete_feedback

`DELETE /rest/servicedeskapi/request/{requestIdOrKey}/feedback` — Delete feedback

- Request: [[JSM - Delete feedback]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
