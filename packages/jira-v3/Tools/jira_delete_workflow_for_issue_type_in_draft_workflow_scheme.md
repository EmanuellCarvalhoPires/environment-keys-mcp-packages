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
tool: jira_delete_workflow_for_issue_type_in_draft_workflow_scheme
title: "Jira v3 - Delete workflow for issue type in draft workflow scheme"
kind: request
request: "[[Jira v3 - Delete workflow for issue type in draft workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType} · Delete workflow for issue type in draft workflow scheme. Deletes the issue type-workflow mapping for an issue type in a workflow scheme's draft. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme that the draft belongs to."
  "issueType":
    type: string
    required: true
    description: "The ID of the issue type."
writes: true
expose: false
---
# jira_delete_workflow_for_issue_type_in_draft_workflow_scheme

`DELETE /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}` — Delete workflow for issue type in draft workflow scheme

- Request: [[Jira v3 - Delete workflow for issue type in draft workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
