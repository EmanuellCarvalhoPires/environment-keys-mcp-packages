---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_worklogs
title: "Jira v3 - Get worklogs"
kind: request
request: "[[Jira v3 - Get worklogs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/worklog/list · Get worklogs. Returns worklog details for a list of worklog IDs. The returned list of worklogs is limited to 1000 items. Permissions required: Permission to access Jira, however, worklogs are only returned where either of the following is true: the worklog is set as Viewable by All Users. Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about worklogs in the response. This parameter accepts properties that returns the properties of each worklog."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_worklogs

`POST /rest/api/3/worklog/list` — Get worklogs

- Request: [[Jira v3 - Get worklogs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
