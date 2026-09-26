---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_default_workflow
title: "Jira v3 - Update default workflow"
kind: request
request: "[[Jira v3 - Update default workflow]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/workflowscheme/{id}/default · Update default workflow. Sets the default workflow for a workflow scheme. Note that active workflow schemes cannot be edited. If the workflow scheme is active, set updateDraftIfNeeded to true in the request object and a draft workflow scheme is created or updated with the new default workflow. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_default_workflow

`PUT /rest/api/3/workflowscheme/{id}/default` — Update default workflow

- Request: [[Jira v3 - Update default workflow]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
