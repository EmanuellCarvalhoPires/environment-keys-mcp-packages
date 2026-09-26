---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_issue
title: "Jira v3 - Delete issue"
kind: request
request: "[[Jira v3 - Delete issue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issue/{issueIdOrKey} · Delete issue. Deletes an issue. An issue cannot be deleted if it has one or more subtasks. To delete an issue with subtasks, set deleteSubtasks. This causes the issue's subtasks to be deleted with the issue. This operation can be accessed anonymously. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "deleteSubtasks":
    type: string
    required: false
    description: "Whether the issue's subtasks are deleted when the issue is deleted."
writes: true
expose: false
---
# jira_delete_issue

`DELETE /rest/api/3/issue/{issueIdOrKey}` — Delete issue

- Request: [[Jira v3 - Delete issue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
