---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_move_worklogs
title: "Jira v3 - Bulk move worklogs"
kind: request
request: "[[Jira v3 - Bulk move worklogs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/{issueIdOrKey}/worklog/move · Bulk move worklogs. Moves a list of worklogs from one issue to another. This is an experimental API with several limitations: You can't move more than 5000 worklogs at once. You can't move worklogs containing an attachment. You can't move worklogs restricted by project roles. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "Value of issueIdOrKey in the path."
  "adjustEstimate":
    type: string
    required: false
    description: "Defines how to update the issues' time estimate, the options are: leave Leaves the estimate unchanged."
  "overrideEditableFlag":
    type: string
    required: false
    description: "Whether the work log entry should be moved to and from the issues even if the issues are not editable, because jira.issue.editable set to false or missing. For example, the issue is closed."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_move_worklogs

`POST /rest/api/3/issue/{issueIdOrKey}/worklog/move` — Bulk move worklogs

- Request: [[Jira v3 - Bulk move worklogs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
