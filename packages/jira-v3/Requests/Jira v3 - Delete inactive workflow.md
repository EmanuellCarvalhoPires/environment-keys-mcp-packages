---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/workflow/{entityId}"
category: "Workflows"
writes_data: true
tool_note: "[[jira_delete_inactive_workflow]]"
---
# Jira v3 - Delete inactive workflow

**Delete inactive workflow** — `DELETE /rest/api/3/workflow/{entityId}`

- Run by the tool [[jira_delete_inactive_workflow]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/workflow/{{param:entityId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `entityId` (path, string, required) — The entity ID of the workflow.

## Original description

Deletes a workflow.

The workflow cannot be deleted if it is:

 *  an active workflow.
 *  a system workflow.
 *  associated with any workflow scheme.
 *  associated with any draft workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
