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
tool: jira_get_draft_workflow_scheme
title: "Jira v3 - Get draft workflow scheme"
kind: request
request: "[[Jira v3 - Get draft workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflowscheme/{id}/draft · Get draft workflow scheme. Returns the draft workflow scheme for an active workflow scheme. Draft workflow schemes allow changes to be made to the active workflow schemes: When an active workflow scheme is updated, a draft copy is created. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the active workflow scheme that the draft was created from."
writes: false
expose: false
---
# jira_get_draft_workflow_scheme

`GET /rest/api/3/workflowscheme/{id}/draft` — Get draft workflow scheme

- Request: [[Jira v3 - Get draft workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
