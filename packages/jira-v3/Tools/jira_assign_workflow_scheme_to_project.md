---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-project-associations
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_assign_workflow_scheme_to_project
title: "Jira v3 - Assign workflow scheme to project"
kind: request
request: "[[Jira v3 - Assign workflow scheme to project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/workflowscheme/project · Assign workflow scheme to project. Assigns a workflow scheme to a project. This operation is performed only when there are no issues in the project. Workflow schemes can only be assigned to classic projects. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_assign_workflow_scheme_to_project

`PUT /rest/api/3/workflowscheme/project` — Assign workflow scheme to project

- Request: [[Jira v3 - Assign workflow scheme to project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
