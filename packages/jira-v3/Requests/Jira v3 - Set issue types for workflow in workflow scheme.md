---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/workflowscheme/{id}/draft/workflow"
category: "Workflow scheme drafts"
writes_data: true
tool_note: "[[jira_set_issue_types_for_workflow_in_workflow_scheme]]"
---
# Jira v3 - Set issue types for workflow in workflow scheme

**Set issue types for workflow in workflow scheme** — `PUT /rest/api/3/workflowscheme/{id}/draft/workflow`

- Run by the tool [[jira_set_issue_types_for_workflow_in_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft/workflow?workflowName={{param:workflowName}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme that the draft belongs to.
- `workflowName` (query, string, required) — The name of the workflow.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issueTypes": [
    "10000"
  ],
  "updateDraftIfNeeded": true,
  "workflow": "jira"
}
```

## Original description

Sets the issue types for a workflow in a workflow scheme's draft. The workflow can also be set as the default workflow for the draft workflow scheme. Unmapped issues types are mapped to the default workflow.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
