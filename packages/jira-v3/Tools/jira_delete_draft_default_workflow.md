---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_draft_default_workflow
title: "Jira v3 - Delete draft default workflow"
kind: request
request: "[[Jira v3 - Delete draft default workflow]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/workflowscheme/{id}/draft/default · Delete draft default workflow. Resets the default workflow for a workflow scheme's draft. That is, the default workflow is set to Jira's system workflow (the jira workflow). Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme that the draft belongs to."
writes: true
expose: false
---
# jira_delete_draft_default_workflow

`DELETE /rest/api/3/workflowscheme/{id}/draft/default` — Delete draft default workflow

- Request: [[Jira v3 - Delete draft default workflow]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
