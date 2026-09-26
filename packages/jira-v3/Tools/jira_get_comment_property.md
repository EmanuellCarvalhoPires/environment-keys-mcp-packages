---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comment-properties
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_comment_property
title: "Jira v3 - Get comment property"
kind: request
request: "[[Jira v3 - Get comment property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/comment/{commentId}/properties/{propertyKey} · Get comment property. Returns the value of a comment property. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project. If issue-level security is configured, issue-level security permission to view the issue. Writes data: no."
params:
  "commentId":
    type: string
    required: true
    description: "The ID of the comment."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property."
writes: false
expose: false
---
# jira_get_comment_property

`GET /rest/api/3/comment/{commentId}/properties/{propertyKey}` — Get comment property

- Request: [[Jira v3 - Get comment property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
