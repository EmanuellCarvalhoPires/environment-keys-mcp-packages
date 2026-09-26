---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-attachments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_attachment_content
title: "Jira v3 - Get attachment content"
kind: request
request: "[[Jira v3 - Get attachment content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/attachment/content/{id} · Get attachment content. Returns the contents of an attachment. A Range header can be set to define a range of bytes within the attachment to download. See the HTTP Range header standard for details. To return a thumbnail of the attachment, use Get attachment thumbnail. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment."
  "redirect":
    type: string
    required: false
    description: "Whether a redirect is provided for the attachment download. Clients that do not automatically follow redirects can set this to false to avoid making multiple requests to download the attachment."
writes: false
expose: false
---
# jira_get_attachment_content

`GET /rest/api/3/attachment/content/{id}` — Get attachment content

- Request: [[Jira v3 - Get attachment content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
