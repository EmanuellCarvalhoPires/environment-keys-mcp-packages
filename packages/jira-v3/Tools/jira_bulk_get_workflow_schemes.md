---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_bulk_get_workflow_schemes
title: "Jira v3 - Bulk get workflow schemes"
kind: request
request: "[[Jira v3 - Bulk get workflow schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflowscheme/read · Bulk get workflow schemes. Returns a list of workflow schemes by providing workflow scheme IDs or project IDs. Permissions required: Administer Jira global permission to access all, including project-scoped, workflow schemes Administer projects project permissions to access project-scoped workflow schemes Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_bulk_get_workflow_schemes

`POST /rest/api/3/workflowscheme/read` — Bulk get workflow schemes

- Request: [[Jira v3 - Bulk get workflow schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
