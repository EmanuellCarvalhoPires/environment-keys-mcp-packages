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
tool: jira_set_issue_types_for_workflow_in_workflow_scheme_put
title: "Jira v3 - Set issue types for workflow in workflow scheme (PUT)"
kind: request
request: "[[Jira v3 - Set issue types for workflow in workflow scheme (PUT)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/workflowscheme/{id}/workflow · Set issue types for workflow in workflow scheme. Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the default workflow for the workflow scheme. Unmapped issues types are mapped to the default workflow. Note that active workflow schemes cannot be edited. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme."
  "workflowName":
    type: string
    required: true
    description: "The name of the workflow."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_issue_types_for_workflow_in_workflow_scheme_put

`PUT /rest/api/3/workflowscheme/{id}/workflow` — Set issue types for workflow in workflow scheme

- Request: [[Jira v3 - Set issue types for workflow in workflow scheme (PUT)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
