---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/list
  - api/effect/read
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_available_workflow_capabilities
title: "Jira v3 - Get available workflow capabilities"
kind: request
request: "[[Jira v3 - Get available workflow capabilities]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflows/capabilities · Get available workflow capabilities. Get the list of workflow capabilities for a specific workflow using either the workflow ID, or the project and issue type ID pair. The response includes the scope of the workflow, defined as global/project-based, and a list of project types that the workflow is scoped to. Writes data: no."
params:
  "workflowId":
    type: string
    required: false
    description: "Query parameter workflowId."
  "projectId":
    type: string
    required: false
    description: "Query parameter projectId."
  "issueTypeId":
    type: string
    required: false
    description: "Query parameter issueTypeId."
writes: false
expose: false
---
# jira_get_available_workflow_capabilities

`GET /rest/api/3/workflows/capabilities` — Get available workflow capabilities

- Request: [[Jira v3 - Get available workflow capabilities]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
