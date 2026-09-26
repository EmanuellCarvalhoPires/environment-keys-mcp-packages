---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_available_transitions
title: "Jira v3 - Get available transitions"
kind: request
request: "[[Jira v3 - Get available transitions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/bulk/issues/transition · Get available transitions. Use this API to retrieve a list of transitions available for the specified issues that can be used or bulk transition operations. You can submit either single or multiple issues in the query to obtain the available transitions. Writes data: no."
params:
  "issueIdsOrKeys":
    type: string
    required: true
    description: "Comma (,) separated Ids or keys of the issues to get transitions available for them."
  "endingBefore":
    type: string
    required: false
    description: "(Optional)The end cursor for use in pagination."
  "startingAfter":
    type: string
    required: false
    description: "(Optional)The start cursor for use in pagination."
writes: false
expose: false
---
# jira_get_available_transitions

`GET /rest/api/3/bulk/issues/transition` — Get available transitions

- Request: [[Jira v3 - Get available transitions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
