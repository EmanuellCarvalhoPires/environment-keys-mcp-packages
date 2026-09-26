---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_comment
title: "Jira v3 - Get comment"
kind: request
request: "[[Jira v3 - Get comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/comment/{id} · Get comment. Returns a comment. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project containing the comment. If issue-level security is configured, issue-level security permission to view the issue. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "id":
    type: string
    required: true
    description: "The ID of the comment."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about comments in the response. This parameter accepts renderedBody, which returns the comment body rendered in HTML."
writes: false
expose: false
---
# jira_get_comment

`GET /rest/api/3/issue/{issueIdOrKey}/comment/{id}` — Get comment

- Request: [[Jira v3 - Get comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
