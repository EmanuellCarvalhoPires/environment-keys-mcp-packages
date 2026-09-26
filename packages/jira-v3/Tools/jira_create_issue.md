---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_create_issue
title: "Jira v3 - Create issue"
kind: request
request: "[[Jira v3 - Create issue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue · Create issue. Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask. A transition may be applied, to move the issue or subtask to a workflow step other than the default start step, and issue properties set. Writes data: yes."
params:
  "updateHistory":
    type: string
    required: false
    description: "Whether the project in which the issue is created is added to the user's Recently viewed project list, as shown under Projects in Jira."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: true
---
# jira_create_issue

`POST /rest/api/3/issue` — Create issue

- Request: [[Jira v3 - Create issue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
