---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_attachment_content
title: "JSM - Get attachment content"
kind: request
request: "[[JSM - Get attachment content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment/{attachmentId} · Get attachment content. Returns the contents of an attachment. To return a thumbnail of the attachment, use servicedeskapi/request/\\{issueIdOrKey\\}/attachment/\\{attachmentId\\}/thumbnail. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key for the customer request the attachment is associated with"
  "attachmentId":
    type: string
    required: true
    description: "The ID for the attachment"
writes: false
expose: false
---
# jsm_get_attachment_content

`GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment/{attachmentId}` — Get attachment content

- Request: [[JSM - Get attachment content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
