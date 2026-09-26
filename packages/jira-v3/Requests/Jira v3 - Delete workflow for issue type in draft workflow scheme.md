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
path: "/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}"
category: "Workflow scheme drafts"
writes_data: true
tool_note: "[[jira_delete_workflow_for_issue_type_in_draft_workflow_scheme]]"
---
# Jira v3 - Delete workflow for issue type in draft workflow scheme

**Delete workflow for issue type in draft workflow scheme** — `DELETE /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}`

- Run by the tool [[jira_delete_workflow_for_issue_type_in_draft_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft/issuetype/{{param:issueType}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme that the draft belongs to.
- `issueType` (path, string, required) — The ID of the issue type.

## Original description

Deletes the issue type-workflow mapping for an issue type in a workflow scheme's draft.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
