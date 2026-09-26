---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-attachments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_attachment_metadata
title: "Jira v3 - Get attachment metadata"
kind: request
request: "[[Jira v3 - Get attachment metadata]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/attachment/{id} · Get attachment metadata. Returns the metadata for an attachment. Note that the attachment itself is not returned. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project that the issue is in. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment."
writes: false
expose: false
---
# jira_get_attachment_metadata

`GET /rest/api/3/attachment/{id}` — Get attachment metadata

- Request: [[Jira v3 - Get attachment metadata]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
