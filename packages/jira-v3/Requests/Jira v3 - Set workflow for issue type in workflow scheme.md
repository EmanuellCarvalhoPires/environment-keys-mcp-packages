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
path: "/rest/api/3/workflowscheme/{id}/issuetype/{issueType}"
category: "Workflow schemes"
writes_data: true
tool_note: "[[jira_set_workflow_for_issue_type_in_workflow_scheme]]"
---
# Jira v3 - Set workflow for issue type in workflow scheme

**Set workflow for issue type in workflow scheme** — `PUT /rest/api/3/workflowscheme/{id}/issuetype/{issueType}`

- Run by the tool [[jira_set_workflow_for_issue_type_in_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/issuetype/{{param:issueType}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme.
- `issueType` (path, string, required) — The ID of the issue type.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issueType": "10000",
  "updateDraftIfNeeded": false,
  "workflow": "jira"
}
```

## Original description

Sets the workflow for an issue type in a workflow scheme.

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or updated with the new issue type-workflow mapping. The draft workflow scheme can be published in Jira.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
