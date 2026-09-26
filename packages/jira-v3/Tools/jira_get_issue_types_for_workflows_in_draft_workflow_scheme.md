---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_types_for_workflows_in_draft_workflow_scheme
title: "Jira v3 - Get issue types for workflows in draft workflow scheme"
kind: request
request: "[[Jira v3 - Get issue types for workflows in draft workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflowscheme/{id}/draft/workflow · Get issue types for workflows in draft workflow scheme. Returns the workflow-issue type mappings for a workflow scheme's draft. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme that the draft belongs to."
  "workflowName":
    type: string
    required: false
    description: "The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow."
writes: false
expose: false
---
# jira_get_issue_types_for_workflows_in_draft_workflow_scheme

`GET /rest/api/3/workflowscheme/{id}/draft/workflow` — Get issue types for workflows in draft workflow scheme

- Request: [[Jira v3 - Get issue types for workflows in draft workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
