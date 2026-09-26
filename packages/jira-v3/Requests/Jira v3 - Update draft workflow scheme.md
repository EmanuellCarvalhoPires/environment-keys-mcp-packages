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
path: "/rest/api/3/workflowscheme/{id}/draft"
category: "Workflow scheme drafts"
writes_data: true
tool_note: "[[jira_update_draft_workflow_scheme]]"
---
# Jira v3 - Update draft workflow scheme

**Update draft workflow scheme** — `PUT /rest/api/3/workflowscheme/{id}/draft`

- Run by the tool [[jira_update_draft_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the active workflow scheme that the draft was created from.
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

Updates a draft workflow scheme. If a draft workflow scheme does not exist for the active workflow scheme, then a draft is created. Note that an active workflow scheme can only have one draft workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
