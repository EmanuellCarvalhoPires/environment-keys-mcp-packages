---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_statuses_for_project
title: "Jira v3 - Get all statuses for project"
kind: request
request: "[[Jira v3 - Get all statuses for project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/statuses · Get all statuses for project. Returns the valid statuses for a project. The statuses are grouped by issue type, as each project has a set of valid issue types and each issue type has a set of valid statuses. This operation can be accessed anonymously. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
writes: false
expose: false
---
# jira_get_all_statuses_for_project

`GET /rest/api/3/project/{projectIdOrKey}/statuses` — Get all statuses for project

- Request: [[Jira v3 - Get all statuses for project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
