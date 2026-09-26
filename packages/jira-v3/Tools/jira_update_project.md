---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_project
title: "Jira v3 - Update project"
kind: request
request: "[[Jira v3 - Update project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/project/{projectIdOrKey} · Update project. Updates the project details of a project. All parameters are optional in the body of the request. Schemes will only be updated if they are included in the request, any omitted schemes will be left unchanged. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_project

`PUT /rest/api/3/project/{projectIdOrKey}` — Update project

- Request: [[Jira v3 - Update project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
