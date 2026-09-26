---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_comment
title: "Jira v3 - Delete comment"
kind: request
request: "[[Jira v3 - Delete comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issue/{issueIdOrKey}/comment/{id} · Delete comment. Deletes a comment. Permissions required: Browse projects project permission for the project that the issue containing the comment is in. If issue-level security is configured, issue-level security permission to view the issue. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "id":
    type: string
    required: true
    description: "The ID of the comment."
writes: true
expose: false
---
# jira_delete_comment

`DELETE /rest/api/3/issue/{issueIdOrKey}/comment/{id}` — Delete comment

- Request: [[Jira v3 - Delete comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
