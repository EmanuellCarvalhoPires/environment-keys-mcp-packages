---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflowscheme/{id}/draft/workflow"
category: "Workflow scheme drafts"
writes_data: false
tool_note: "[[jira_get_issue_types_for_workflows_in_draft_workflow_scheme]]"
---
# Jira v3 - Get issue types for workflows in draft workflow scheme

**Get issue types for workflows in draft workflow scheme** — `GET /rest/api/3/workflowscheme/{id}/draft/workflow`

- Run by the tool [[jira_get_issue_types_for_workflows_in_draft_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft/workflow?workflowName={{param:workflowName}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme that the draft belongs to.
- `workflowName` (query, string, optional) — The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow.

## Original description

Returns the workflow-issue type mappings for a workflow scheme's draft.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
