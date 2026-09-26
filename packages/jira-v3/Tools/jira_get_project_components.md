---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_components
title: "Jira v3 - Get project components"
kind: request
request: "[[Jira v3 - Get project components]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/components · Get project components. Returns all components in a project. See the Get project components paginated resource if you want to get a full list of components with pagination. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "componentSource":
    type: string
    required: false
    description: "The source of the components to return. Can be jira (default), compass or auto. When auto is specified, the API will return connected Compass components if the project is opted into Compass, otherwise…"
writes: false
expose: false
---
# jira_get_project_components

`GET /rest/api/3/project/{projectIdOrKey}/components` — Get project components

- Request: [[Jira v3 - Get project components]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
