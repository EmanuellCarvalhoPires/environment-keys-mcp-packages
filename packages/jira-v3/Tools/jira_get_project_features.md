---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-features
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_features
title: "Jira v3 - Get project features"
kind: request
request: "[[Jira v3 - Get project features]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/features · Get project features. Returns the list of features for a project. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The ID or (case-sensitive) key of the project."
writes: false
expose: false
---
# jira_get_project_features

`GET /rest/api/3/project/{projectIdOrKey}/features` — Get project features

- Request: [[Jira v3 - Get project features]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
