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
tool: jira_update_draft_default_workflow
title: "Jira v3 - Update draft default workflow"
kind: request
request: "[[Jira v3 - Update draft default workflow]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/workflowscheme/{id}/draft/default · Update draft default workflow. Sets the default workflow for a workflow scheme's draft. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme that the draft belongs to."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_draft_default_workflow

`PUT /rest/api/3/workflowscheme/{id}/draft/default` — Update draft default workflow

- Request: [[Jira v3 - Update draft default workflow]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
