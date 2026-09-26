---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_attachment_thumbnail
title: "JSM - Get attachment thumbnail"
kind: request
request: "[[JSM - Get attachment thumbnail]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment/{attachmentId}/thumbnail · Get attachment thumbnail. Returns the thumbnail of an attachment. To return the attachment contents, use servicedeskapi/request/\\{issueIdOrKey\\}/attachment/\\{attachmentId\\}. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key for the customer request the attachment is associated with"
  "attachmentId":
    type: string
    required: true
    description: "The ID of the attachment."
writes: false
expose: false
---
# jsm_get_attachment_thumbnail

`GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment/{attachmentId}/thumbnail` — Get attachment thumbnail

- Request: [[JSM - Get attachment thumbnail]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
