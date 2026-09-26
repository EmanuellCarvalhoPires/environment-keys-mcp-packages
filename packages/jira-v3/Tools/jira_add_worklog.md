---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_add_worklog
title: "Jira v3 - Add worklog"
kind: request
request: "[[Jira v3 - Add worklog]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/{issueIdOrKey}/worklog · Add worklog. Adds a worklog to an issue. Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see Configuring time tracking. This operation can be accessed anonymously. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key the issue."
  "notifyUsers":
    type: string
    required: false
    description: "Whether users watching the issue are notified by email."
  "adjustEstimate":
    type: string
    required: false
    description: "Defines how to update the issue's time estimate, the options are: new Sets the estimate to a specific value, defined in newEstimate. leave Leaves the estimate unchanged."
  "newEstimate":
    type: string
    required: false
    description: "The value to set as the issue's remaining time estimate, as days (\\d), hours (\\h), or minutes (\\m or \\). For example, 2d. Required when adjustEstimate is new."
  "reduceBy":
    type: string
    required: false
    description: "The amount to reduce the issue's remaining estimate by, as days (\\d), hours (\\h), or minutes (\\m). For example, 2d. Required when adjustEstimate is manual."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about work logs in the response. This parameter accepts properties, which returns worklog properties."
  "overrideEditableFlag":
    type: string
    required: false
    description: "Whether the worklog entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_add_worklog

`POST /rest/api/3/issue/{issueIdOrKey}/worklog` — Add worklog

- Request: [[Jira v3 - Add worklog]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
