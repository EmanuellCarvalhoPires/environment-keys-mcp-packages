---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_add_comment
title: "Jira v3 - Add comment"
kind: request
request: "[[Jira v3 - Add comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/{issueIdOrKey}/comment · Add comment. Adds a comment to an issue. This operation can be accessed anonymously. Permissions required: Browse projects and Add comments project permission for the project that the issue containing the comment is in. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about comments in the response. This parameter accepts renderedBody, which returns the comment body rendered in HTML."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: true
---
# jira_add_comment

`POST /rest/api/3/issue/{issueIdOrKey}/comment` — Add comment

- Request: [[Jira v3 - Add comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
