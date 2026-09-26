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
path: "/rest/api/3/workflowscheme/{id}/draft/default"
category: "Workflow scheme drafts"
writes_data: true
tool_note: "[[jira_delete_draft_default_workflow]]"
---
# Jira v3 - Delete draft default workflow

**Delete draft default workflow** — `DELETE /rest/api/3/workflowscheme/{id}/draft/default`

- Run by the tool [[jira_delete_draft_default_workflow]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft/default
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme that the draft belongs to.

## Original description

Resets the default workflow for a workflow scheme's draft. That is, the default workflow is set to Jira's system workflow (the *jira* workflow).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
