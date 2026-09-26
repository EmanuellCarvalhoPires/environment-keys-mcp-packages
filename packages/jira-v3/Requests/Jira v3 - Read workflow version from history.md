---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflow/history"
category: "Workflows"
writes_data: true
tool_note: "[[jira_read_workflow_version_from_history]]"
---
# Jira v3 - Read workflow version from history

**Read workflow version from history** — `POST /rest/api/3/workflow/history`

- Run by the tool [[jira_read_workflow_version_from_history]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflow/history
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "version": 4,
  "workflowId": "c5ef565c-1b1e-427e-bc3b-e677b0dc027c"
}
```

## Original description

Returns a workflow and related statuses for a specified workflow id and version number.

**Note:** Stored workflow data expires after 60 days. Additionally, no data from before the 30th of October 2025 is available.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to access all, including project-scoped, workflows
 *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows
