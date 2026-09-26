---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/workflowscheme/{id}/draft"
category: "Workflow scheme drafts"
writes_data: true
tool_note: "[[jira_delete_draft_workflow_scheme]]"
---
# Jira v3 - Delete draft workflow scheme

**Delete draft workflow scheme** — `DELETE /rest/api/3/workflowscheme/{id}/draft`

- Run by the tool [[jira_delete_draft_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the active workflow scheme that the draft was created from.

## Original description

Deletes a draft workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
