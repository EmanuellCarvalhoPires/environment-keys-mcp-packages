---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-attachments
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_attachment
title: "Jira v3 - Delete attachment"
kind: request
request: "[[Jira v3 - Delete attachment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/attachment/{id} · Delete attachment. Deletes an attachment from an issue. This operation can be accessed anonymously. Permissions required: For the project holding the issue containing the attachment: Delete own attachments project permission to delete an attachment created by the calling user. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment."
writes: true
expose: false
---
# jira_delete_attachment

`DELETE /rest/api/3/attachment/{id}` — Delete attachment

- Request: [[Jira v3 - Delete attachment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
