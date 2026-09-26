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
tool: jira_get_draft_default_workflow
title: "Jira v3 - Get draft default workflow"
kind: request
request: "[[Jira v3 - Get draft default workflow]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflowscheme/{id}/draft/default · Get draft default workflow. Returns the default workflow for a workflow scheme's draft. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme that the draft belongs to."
writes: false
expose: false
---
# jira_get_draft_default_workflow

`GET /rest/api/3/workflowscheme/{id}/draft/default` — Get draft default workflow

- Request: [[Jira v3 - Get draft default workflow]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
