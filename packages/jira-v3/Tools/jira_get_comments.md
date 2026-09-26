---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_comments
title: "Jira v3 - Get comments"
kind: request
request: "[[Jira v3 - Get comments]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/comment · Get comments. Returns all comments for an issue. This operation can be accessed anonymously. Permissions required: Comments are included in the response where the user has: Browse projects project permission for the project containing the comment. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "orderBy":
    type: string
    required: false
    description: "Order the results by a field. Accepts created to sort comments by their created date."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about comments in the response. This parameter accepts renderedBody, which returns the comment body rendered in HTML."
writes: false
expose: true
---
# jira_get_comments

`GET /rest/api/3/issue/{issueIdOrKey}/comment` — Get comments

- Request: [[Jira v3 - Get comments]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
