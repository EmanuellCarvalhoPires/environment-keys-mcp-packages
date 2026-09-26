---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_recent_projects
title: "Jira v3 - Get recent projects"
kind: request
request: "[[Jira v3 - Get recent projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/recent · Get recent projects. Returns a list of up to 20 projects recently viewed by the user that are still visible to the user. This operation can be accessed anonymously. Permissions required: Projects are returned only where the user has one of: Browse Projects project permission for the project. Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include: description Returns the project description."
  "properties":
    type: string
    required: false
    description: "EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list. Invalid property names are ignored."
writes: false
expose: false
---
# jira_get_recent_projects

`GET /rest/api/3/project/recent` — Get recent projects

- Request: [[Jira v3 - Get recent projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
