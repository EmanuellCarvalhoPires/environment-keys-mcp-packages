---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_delete_worklogs
title: "Jira v3 - Bulk delete worklogs"
kind: request
request: "[[Jira v3 - Bulk delete worklogs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issue/{issueIdOrKey}/worklog · Bulk delete worklogs. Deletes a list of worklogs from an issue. This is an experimental API with limitations: You can't delete more than 5000 worklogs at once. No notifications will be sent for deleted worklogs. Time tracking must be enabled in Jira, otherwise this operation returns an error. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "adjustEstimate":
    type: string
    required: false
    description: "Defines how to update the issue's time estimate, the options are: leave Leaves the estimate unchanged. auto Reduces the estimate by the aggregate value of timeSpent across all worklogs being deleted."
  "overrideEditableFlag":
    type: string
    required: false
    description: "Whether the work log entries should be removed to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_delete_worklogs

`DELETE /rest/api/3/issue/{issueIdOrKey}/worklog` — Bulk delete worklogs

- Request: [[Jira v3 - Bulk delete worklogs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
