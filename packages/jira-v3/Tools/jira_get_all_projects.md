---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/list
  - api/effect/read
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_all_projects
title: "Jira v3 - Get all projects"
kind: request
request: "[[Jira v3 - Get all projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project · Get all projects. Returns all projects visible to the user. Deprecated, use Get projects paginated that supports search and pagination. This operation can be accessed anonymously. Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include: description Returns the project description."
  "recent":
    type: string
    required: false
    description: "Returns the user's most recently accessed projects. You may specify the number of results to return up to a maximum of 20."
  "properties":
    type: string
    required: false
    description: "A list of project properties to return for the project. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_get_all_projects

`GET /rest/api/3/project` — Get all projects

- Request: [[Jira v3 - Get all projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
