---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_workflow_for_issue_type_in_draft_workflow_scheme
title: "Jira v3 - Get workflow for issue type in draft workflow scheme"
kind: request
request: "[[Jira v3 - Get workflow for issue type in draft workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType} · Get workflow for issue type in draft workflow scheme. Returns the issue type-workflow mapping for an issue type in a workflow scheme's draft. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme that the draft belongs to."
  "issueType":
    type: string
    required: true
    description: "The ID of the issue type."
writes: false
expose: false
---
# jira_get_workflow_for_issue_type_in_draft_workflow_scheme

`GET /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}` — Get workflow for issue type in draft workflow scheme

- Request: [[Jira v3 - Get workflow for issue type in draft workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
