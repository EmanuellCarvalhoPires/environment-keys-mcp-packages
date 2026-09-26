---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/action
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_workflow_scheme
title: "Jira v3 - Update workflow scheme"
kind: request
request: "[[Jira v3 - Update workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflowscheme/update · Update workflow scheme. Updates company-managed and team-managed project workflow schemes. This API doesn't have a concept of draft, so any changes made to a workflow scheme are immediately available. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_workflow_scheme

`POST /rest/api/3/workflowscheme/update` — Update workflow scheme

- Request: [[Jira v3 - Update workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
