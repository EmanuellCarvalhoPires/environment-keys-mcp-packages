---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project
title: "Jira v3 - Get project"
kind: request
request: "[[Jira v3 - Get project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey} · Get project. Returns the project details for a project. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list."
  "properties":
    type: string
    required: false
    description: "A list of project properties to return for the project. This parameter accepts a comma-separated list."
writes: false
expose: true
---
# jira_get_project

`GET /rest/api/3/project/{projectIdOrKey}` — Get project

- Request: [[Jira v3 - Get project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
