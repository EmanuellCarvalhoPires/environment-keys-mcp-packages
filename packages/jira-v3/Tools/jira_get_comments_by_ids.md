---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_comments_by_ids
title: "Jira v3 - Get comments by IDs"
kind: request
request: "[[Jira v3 - Get comments by IDs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/comment/list · Get comments by IDs. Returns a paginated list of comments specified by a list of comment IDs. This operation can be accessed anonymously. Permissions required: Comments are returned where the user: has Browse projects project permission for the project containing the comment. Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about comments in the response. This parameter accepts a comma-separated list."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_comments_by_ids

`POST /rest/api/3/comment/list` — Get comments by IDs

- Request: [[Jira v3 - Get comments by IDs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
