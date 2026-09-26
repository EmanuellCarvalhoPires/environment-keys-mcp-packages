---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_default_workflow
title: "Jira v3 - Delete default workflow"
kind: request
request: "[[Jira v3 - Delete default workflow]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/workflowscheme/{id}/default · Delete default workflow. Resets the default workflow for a workflow scheme. That is, the default workflow is set to Jira's system workflow (the jira workflow). Note that active workflow schemes cannot be edited. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme."
  "updateDraftIfNeeded":
    type: string
    required: false
    description: "Set to true to create or update the draft of a workflow scheme and delete the mapping from the draft, when the workflow scheme cannot be edited. Defaults to false."
writes: true
expose: false
---
# jira_delete_default_workflow

`DELETE /rest/api/3/workflowscheme/{id}/default` — Delete default workflow

- Request: [[Jira v3 - Delete default workflow]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
