---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comment-properties
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_comment_property_keys
title: "Jira v3 - Get comment property keys"
kind: request
request: "[[Jira v3 - Get comment property keys]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/comment/{commentId}/properties · Get comment property keys. Returns the keys of all the properties of a comment. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project. If issue-level security is configured, issue-level security permission to view the issue. Writes data: no."
params:
  "commentId":
    type: string
    required: true
    description: "The ID of the comment."
writes: false
expose: false
---
# jira_get_comment_property_keys

`GET /rest/api/3/comment/{commentId}/properties` — Get comment property keys

- Request: [[Jira v3 - Get comment property keys]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
