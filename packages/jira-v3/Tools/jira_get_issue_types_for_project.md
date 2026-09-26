---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_types_for_project
title: "Jira v3 - Get issue types for project"
kind: request
request: "[[Jira v3 - Get issue types for project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetype/project · Get issue types for project. Returns issue types for a project. This operation can be accessed anonymously. Permissions required: Browse projects project permission in the relevant project or Administer Jira global permission. Writes data: no."
params:
  "projectId":
    type: string
    required: true
    description: "The ID of the project."
  "level":
    type: string
    required: false
    description: "The level of the issue type to filter by. Use: -1 for Subtask. 0 for Base. 1 for Epic."
writes: false
expose: false
---
# jira_get_issue_types_for_project

`GET /rest/api/3/issuetype/project` — Get issue types for project

- Request: [[Jira v3 - Get issue types for project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
