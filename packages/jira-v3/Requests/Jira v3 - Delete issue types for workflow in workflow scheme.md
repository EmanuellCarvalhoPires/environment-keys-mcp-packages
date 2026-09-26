---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/workflowscheme/{id}/workflow"
category: "Workflow schemes"
writes_data: true
tool_note: "[[jira_delete_issue_types_for_workflow_in_workflow_scheme]]"
---
# Jira v3 - Delete issue types for workflow in workflow scheme

**Delete issue types for workflow in workflow scheme** — `DELETE /rest/api/3/workflowscheme/{id}/workflow`

- Run by the tool [[jira_delete_issue_types_for_workflow_in_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/workflow?workflowName={{param:workflowName}}&updateDraftIfNeeded={{param:updateDraftIfNeeded}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme.
- `workflowName` (query, string, required) — The name of the workflow.
- `updateDraftIfNeeded` (query, string, optional) — Set to true to create or update the draft of a workflow scheme and delete the mapping from the draft, when the workflow scheme cannot be edited. Defaults to false.

## Original description

Deletes the workflow-issue type mapping for a workflow in a workflow scheme.

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the workflow-issue type mapping deleted. The draft workflow scheme can be published in Jira.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
