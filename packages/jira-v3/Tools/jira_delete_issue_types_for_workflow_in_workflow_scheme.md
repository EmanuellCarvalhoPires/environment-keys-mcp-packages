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
tool: jira_delete_issue_types_for_workflow_in_workflow_scheme
title: "Jira v3 - Delete issue types for workflow in workflow scheme"
kind: request
request: "[[Jira v3 - Delete issue types for workflow in workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/workflowscheme/{id}/workflow · Delete issue types for workflow in workflow scheme. Deletes the workflow-issue type mapping for a workflow in a workflow scheme. Note that active workflow schemes cannot be edited. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme."
  "workflowName":
    type: string
    required: true
    description: "The name of the workflow."
  "updateDraftIfNeeded":
    type: string
    required: false
    description: "Set to true to create or update the draft of a workflow scheme and delete the mapping from the draft, when the workflow scheme cannot be edited. Defaults to false."
writes: true
expose: false
---
# jira_delete_issue_types_for_workflow_in_workflow_scheme

`DELETE /rest/api/3/workflowscheme/{id}/workflow` — Delete issue types for workflow in workflow scheme

- Request: [[Jira v3 - Delete issue types for workflow in workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
