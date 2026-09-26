---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_versions
title: "Jira v3 - Get project versions"
kind: request
request: "[[Jira v3 - Get project versions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/versions · Get project versions. Returns all versions in a project. The response is not paginated. Use Get project versions paginated if you want to get the versions in a project with pagination. This operation can be accessed anonymously. Permissions required: Browse Projects project permission for the project. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts operations, which returns actions that can be performed on the version."
writes: false
expose: false
---
# jira_get_project_versions

`GET /rest/api/3/project/{projectIdOrKey}/versions` — Get project versions

- Request: [[Jira v3 - Get project versions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
