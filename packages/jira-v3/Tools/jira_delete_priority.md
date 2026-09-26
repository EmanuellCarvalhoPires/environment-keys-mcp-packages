---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_priority
title: "Jira v3 - Delete priority"
kind: request
request: "[[Jira v3 - Delete priority]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/priority/{id} · Delete priority. Deletes an issue priority. This operation is asynchronous. Follow the location link in the response to determine the status of the task and use Get task to obtain subsequent updates. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue priority."
writes: true
expose: false
---
# jira_delete_priority

`DELETE /rest/api/3/priority/{id}` — Delete priority

- Request: [[Jira v3 - Delete priority]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
