---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-votes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_votes
title: "Jira v3 - Get votes"
kind: request
request: "[[Jira v3 - Get votes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/votes · Get votes. Returns details about the votes on an issue. This operation requires the Allow users to vote on issues option to be ON. This option is set in General configuration for Jira. See Configuring Jira application options for details. This operation can be accessed anonymously. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
writes: false
expose: false
---
# jira_get_votes

`GET /rest/api/3/issue/{issueIdOrKey}/votes` — Get votes

- Request: [[Jira v3 - Get votes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
