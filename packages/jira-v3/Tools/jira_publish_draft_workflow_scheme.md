---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_publish_draft_workflow_scheme
title: "Jira v3 - Publish draft workflow scheme"
kind: request
request: "[[Jira v3 - Publish draft workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflowscheme/{id}/draft/publish · Publish draft workflow scheme. Publishes a draft workflow scheme. Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to update issues with the original workflow status to the new workflow status. This operation is asynchronous. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme that the draft belongs to."
  "validateOnly":
    type: string
    required: false
    description: "Whether the request only performs a validation."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_publish_draft_workflow_scheme

`POST /rest/api/3/workflowscheme/{id}/draft/publish` — Publish draft workflow scheme

- Request: [[Jira v3 - Publish draft workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
