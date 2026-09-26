---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/workflowscheme/{id}/draft/workflow"
category: "Workflow scheme drafts"
writes_data: true
tool_note: "[[jira_delete_issue_types_for_workflow_in_draft_workflow_scheme]]"
---
# Jira v3 - Delete issue types for workflow in draft workflow scheme

**Delete issue types for workflow in draft workflow scheme** — `DELETE /rest/api/3/workflowscheme/{id}/draft/workflow`

- Run by the tool [[jira_delete_issue_types_for_workflow_in_draft_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft/workflow?workflowName={{param:workflowName}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme that the draft belongs to.
- `workflowName` (query, string, required) — The name of the workflow.

## Original description

Deletes the workflow-issue type mapping for a workflow in a workflow scheme's draft.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
