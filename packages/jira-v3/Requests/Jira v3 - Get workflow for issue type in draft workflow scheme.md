---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}"
category: "Workflow scheme drafts"
writes_data: false
tool_note: "[[jira_get_workflow_for_issue_type_in_draft_workflow_scheme]]"
---
# Jira v3 - Get workflow for issue type in draft workflow scheme

**Get workflow for issue type in draft workflow scheme** — `GET /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}`

- Run by the tool [[jira_get_workflow_for_issue_type_in_draft_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft/issuetype/{{param:issueType}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme that the draft belongs to.
- `issueType` (path, string, required) — The ID of the issue type.

## Original description

Returns the issue type-workflow mapping for an issue type in a workflow scheme's draft.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
