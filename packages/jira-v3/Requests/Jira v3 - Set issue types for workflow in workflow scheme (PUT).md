---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/workflowscheme/{id}/workflow"
category: "Workflow schemes"
writes_data: true
tool_note: "[[jira_set_issue_types_for_workflow_in_workflow_scheme_put]]"
---
# Jira v3 - Set issue types for workflow in workflow scheme (PUT)

**Set issue types for workflow in workflow scheme** — `PUT /rest/api/3/workflowscheme/{id}/workflow`

- Run by the tool [[jira_set_issue_types_for_workflow_in_workflow_scheme_put]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/workflow?workflowName={{param:workflowName}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme.
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

Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the default workflow for the workflow scheme. Unmapped issues types are mapped to the default workflow.

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or updated with the new workflow-issue types mappings. The draft workflow scheme can be published in Jira.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
