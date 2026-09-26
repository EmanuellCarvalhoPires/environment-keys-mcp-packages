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
tool: jira_delete_draft_workflow_scheme
title: "Jira v3 - Delete draft workflow scheme"
kind: request
request: "[[Jira v3 - Delete draft workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/workflowscheme/{id}/draft · Delete draft workflow scheme. Deletes a draft workflow scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the active workflow scheme that the draft was created from."
writes: true
expose: false
---
# jira_delete_draft_workflow_scheme

`DELETE /rest/api/3/workflowscheme/{id}/draft` — Delete draft workflow scheme

- Request: [[Jira v3 - Delete draft workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
