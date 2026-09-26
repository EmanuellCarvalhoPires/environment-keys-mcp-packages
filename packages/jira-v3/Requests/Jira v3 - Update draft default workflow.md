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
path: "/rest/api/3/workflowscheme/{id}/draft/default"
category: "Workflow scheme drafts"
writes_data: true
tool_note: "[[jira_update_draft_default_workflow]]"
---
# Jira v3 - Update draft default workflow

**Update draft default workflow** — `PUT /rest/api/3/workflowscheme/{id}/draft/default`

- Run by the tool [[jira_update_draft_default_workflow]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft/default
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme that the draft belongs to.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "updateDraftIfNeeded": false,
  "workflow": "jira"
}
```

## Original description

Sets the default workflow for a workflow scheme's draft.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
