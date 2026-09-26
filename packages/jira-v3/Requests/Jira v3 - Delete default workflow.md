---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/workflowscheme/{id}/default"
category: "Workflow schemes"
writes_data: true
tool_note: "[[jira_delete_default_workflow]]"
---
# Jira v3 - Delete default workflow

**Delete default workflow** — `DELETE /rest/api/3/workflowscheme/{id}/default`

- Run by the tool [[jira_delete_default_workflow]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/default?updateDraftIfNeeded={{param:updateDraftIfNeeded}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the workflow scheme.
- `updateDraftIfNeeded` (query, string, optional) — Set to true to create or update the draft of a workflow scheme and delete the mapping from the draft, when the workflow scheme cannot be edited. Defaults to false.

## Original description

Resets the default workflow for a workflow scheme. That is, the default workflow is set to Jira's system workflow (the *jira* workflow).

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the default workflow reset. The draft workflow scheme can be published in Jira.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
