---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflowscheme/{id}/issuetype/{issueType}"
category: "Workflow schemes"
writes_data: false
tool_note: "[[jira_get_workflow_for_issue_type_in_workflow_scheme]]"
---
# Jira v3 - Get workflow for issue type in workflow scheme

**Get workflow for issue type in workflow scheme** — `GET /rest/api/3/workflowscheme/{id}/issuetype/{issueType}`

- Run by the tool [[jira_get_workflow_for_issue_type_in_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/issuetype/{{param:issueType}}?returnDraftIfExists={{param:returnDraftIfExists}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme.
- `issueType` (path, string, required) — The ID of the issue type.
- `returnDraftIfExists` (query, string, optional) — Returns the mapping from the workflow scheme's draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned.

## Original description

Returns the issue type-workflow mapping for an issue type in a workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
