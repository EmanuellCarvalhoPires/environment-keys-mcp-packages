---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/search
  - api/effect/read
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_required_status_mappings_for_workflow_scheme_update
title: "Jira v3 - Get required status mappings for workflow scheme update"
kind: request
request: "[[Jira v3 - Get required status mappings for workflow scheme update]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflowscheme/update/mappings · Get required status mappings for workflow scheme update. Gets the required status mappings for the desired changes to a workflow scheme. The results are provided per issue type and workflow. When updating a workflow scheme, status mappings can be provided per issue type, per workflow, or both. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_required_status_mappings_for_workflow_scheme_update

`POST /rest/api/3/workflowscheme/update/mappings` — Get required status mappings for workflow scheme update

- Request: [[Jira v3 - Get required status mappings for workflow scheme update]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
