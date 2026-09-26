---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/priority-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_priority_scheme
title: "Jira v3 - Delete priority scheme"
kind: request
request: "[[Jira v3 - Delete priority scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/priorityscheme/{schemeId} · Delete priority scheme. Deletes a priority scheme. This operation is only available for priority schemes without any associated projects. Any associated projects must be removed from the priority scheme before this operation can be performed. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The priority scheme ID."
writes: true
expose: false
---
# jira_delete_priority_scheme

`DELETE /rest/api/3/priorityscheme/{schemeId}` — Delete priority scheme

- Request: [[Jira v3 - Delete priority scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
