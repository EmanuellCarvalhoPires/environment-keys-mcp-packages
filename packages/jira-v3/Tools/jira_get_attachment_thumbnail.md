---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-attachments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_attachment_thumbnail
title: "Jira v3 - Get attachment thumbnail"
kind: request
request: "[[Jira v3 - Get attachment thumbnail]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/attachment/thumbnail/{id} · Get attachment thumbnail. Returns the thumbnail of an attachment. To return the attachment contents, use Get attachment content. This operation can be accessed anonymously. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment."
  "redirect":
    type: string
    required: false
    description: "Whether a redirect is provided for the attachment download. Clients that do not automatically follow redirects can set this to false to avoid making multiple requests to download the attachment."
  "fallbackToDefault":
    type: string
    required: false
    description: "Whether a default thumbnail is returned when the requested thumbnail is not found."
  "width":
    type: string
    required: false
    description: "The maximum width to scale the thumbnail to."
  "height":
    type: string
    required: false
    description: "The maximum height to scale the thumbnail to."
writes: false
expose: false
---
# jira_get_attachment_thumbnail

`GET /rest/api/3/attachment/thumbnail/{id}` — Get attachment thumbnail

- Request: [[Jira v3 - Get attachment thumbnail]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
