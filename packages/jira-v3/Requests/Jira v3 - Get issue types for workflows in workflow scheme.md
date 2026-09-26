---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflowscheme/{id}/workflow"
category: "Workflow schemes"
writes_data: false
tool_note: "[[jira_get_issue_types_for_workflows_in_workflow_scheme]]"
---
# Jira v3 - Get issue types for workflows in workflow scheme

**Get issue types for workflows in workflow scheme** — `GET /rest/api/3/workflowscheme/{id}/workflow`

- Run by the tool [[jira_get_issue_types_for_workflows_in_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/workflow?workflowName={{param:workflowName}}&returnDraftIfExists={{param:returnDraftIfExists}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme.
- `workflowName` (query, string, optional) — The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow.
- `returnDraftIfExists` (query, string, optional) — Returns the mapping from the workflow scheme's draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned.

## Original description

Returns the workflow-issue type mappings for a workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
