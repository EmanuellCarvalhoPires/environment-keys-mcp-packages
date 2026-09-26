---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_types_for_workflows_in_workflow_scheme
title: "Jira v3 - Get issue types for workflows in workflow scheme"
kind: request
request: "[[Jira v3 - Get issue types for workflows in workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflowscheme/{id}/workflow · Get issue types for workflows in workflow scheme. Returns the workflow-issue type mappings for a workflow scheme. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme."
  "workflowName":
    type: string
    required: false
    description: "The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow."
  "returnDraftIfExists":
    type: string
    required: false
    description: "Returns the mapping from the workflow scheme's draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned."
writes: false
expose: false
---
# jira_get_issue_types_for_workflows_in_workflow_scheme

`GET /rest/api/3/workflowscheme/{id}/workflow` — Get issue types for workflows in workflow scheme

- Request: [[Jira v3 - Get issue types for workflows in workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
