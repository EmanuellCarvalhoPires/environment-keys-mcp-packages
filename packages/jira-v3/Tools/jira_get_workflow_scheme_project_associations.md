---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-project-associations
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_workflow_scheme_project_associations
title: "Jira v3 - Get workflow scheme project associations"
kind: request
request: "[[Jira v3 - Get workflow scheme project associations]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflowscheme/project · Get workflow scheme project associations. Returns a list of the workflow schemes associated with a list of projects. Each returned workflow scheme includes a list of the requested projects associated with it. Any team-managed or non-existent projects in the request are ignored and no errors are returned. Writes data: no."
params:
  "projectId":
    type: string
    required: true
    description: "The ID of a project to return the workflow schemes for. To include multiple projects, provide an ampersand-Jim: oneseparated list. For example, projectId=10000&projectId=10001."
writes: false
expose: false
---
# jira_get_workflow_scheme_project_associations

`GET /rest/api/3/workflowscheme/project` — Get workflow scheme project associations

- Request: [[Jira v3 - Get workflow scheme project associations]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
