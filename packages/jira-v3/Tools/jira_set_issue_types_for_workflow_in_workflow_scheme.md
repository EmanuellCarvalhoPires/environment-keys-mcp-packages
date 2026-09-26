---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_issue_types_for_workflow_in_workflow_scheme
title: "Jira v3 - Set issue types for workflow in workflow scheme"
kind: request
request: "[[Jira v3 - Set issue types for workflow in workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/workflowscheme/{id}/draft/workflow · Set issue types for workflow in workflow scheme. Sets the issue types for a workflow in a workflow scheme's draft. The workflow can also be set as the default workflow for the draft workflow scheme. Unmapped issues types are mapped to the default workflow. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme that the draft belongs to."
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
# jira_set_issue_types_for_workflow_in_workflow_scheme

`PUT /rest/api/3/workflowscheme/{id}/draft/workflow` — Set issue types for workflow in workflow scheme

- Request: [[Jira v3 - Set issue types for workflow in workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
