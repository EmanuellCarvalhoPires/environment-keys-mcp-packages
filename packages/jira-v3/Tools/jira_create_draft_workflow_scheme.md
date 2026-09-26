---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_draft_workflow_scheme
title: "Jira v3 - Create draft workflow scheme"
kind: request
request: "[[Jira v3 - Create draft workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflowscheme/{id}/createdraft · Create draft workflow scheme. Create a draft workflow scheme from an active workflow scheme, by copying the active workflow scheme. Note that an active workflow scheme can only have one draft workflow scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the active workflow scheme that the draft is created from."
writes: true
expose: false
---
# jira_create_draft_workflow_scheme

`POST /rest/api/3/workflowscheme/{id}/createdraft` — Create draft workflow scheme

- Request: [[Jira v3 - Create draft workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
