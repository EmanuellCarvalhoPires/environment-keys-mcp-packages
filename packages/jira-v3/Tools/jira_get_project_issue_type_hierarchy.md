---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_issue_type_hierarchy
title: "Jira v3 - Get project issue type hierarchy"
kind: request
request: "[[Jira v3 - Get project issue type hierarchy]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectId}/hierarchy · Get project issue type hierarchy. Get the issue type hierarchy for a next-gen project. The issue type hierarchy for a project consists of: Epic at level 1 (optional). One or more issue types at level 0 such as Story, Task, or Bug. Writes data: no."
params:
  "projectId":
    type: string
    required: true
    description: "The ID of the project."
writes: false
expose: false
---
# jira_get_project_issue_type_hierarchy

`GET /rest/api/3/project/{projectId}/hierarchy` — Get project issue type hierarchy

- Request: [[Jira v3 - Get project issue type hierarchy]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
