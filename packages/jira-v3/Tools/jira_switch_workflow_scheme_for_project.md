---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_switch_workflow_scheme_for_project
title: "Jira v3 - Switch workflow scheme for project"
kind: request
request: "[[Jira v3 - Switch workflow scheme for project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflowscheme/project/switch · Switch workflow scheme for project. Switches a workflow scheme for a project. Workflow schemes can only be assigned to classic projects. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_switch_workflow_scheme_for_project

`POST /rest/api/3/workflowscheme/project/switch` — Switch workflow scheme for project

- Request: [[Jira v3 - Switch workflow scheme for project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
