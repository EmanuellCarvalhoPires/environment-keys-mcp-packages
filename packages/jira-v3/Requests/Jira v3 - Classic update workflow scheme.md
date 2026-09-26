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
path: "/rest/api/3/workflowscheme/{id}"
category: "Workflow schemes"
writes_data: true
tool_note: "[[jira_classic_update_workflow_scheme]]"
---
# Jira v3 - Classic update workflow scheme

**Classic update workflow scheme** — `PUT /rest/api/3/workflowscheme/{id}`

- Run by the tool [[jira_classic_update_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/workflowscheme/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as schemeId. For example, schemeId=10301.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "defaultWorkflow": "jira",
  "description": "The description of the example workflow scheme.",
  "issueTypeMappings": {
    "10000": "scrum workflow"
  },
  "name": "Example workflow scheme",
  "updateDraftIfNeeded": false
}
```

## Original description

Updates a company-manged project workflow scheme, including the name, default workflow, issue type to project mappings, and more. If the workflow scheme is active (that is, being used by at least one project), then a draft workflow scheme is created or updated instead, provided that `updateDraftIfNeeded` is set to `true`.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
