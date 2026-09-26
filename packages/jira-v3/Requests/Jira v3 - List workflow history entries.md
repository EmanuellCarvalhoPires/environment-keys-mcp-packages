---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflow/history/list"
category: "Workflows"
writes_data: false
tool_note: "[[jira_list_workflow_history_entries]]"
---
# Jira v3 - List workflow history entries

**List workflow history entries** — `POST /rest/api/3/workflow/history/list`

- Run by the tool [[jira_list_workflow_history_entries]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflow/history/list?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "workflowId": "c5ef565c-1b1e-427e-bc3b-e677b0dc027c"
}
```

## Original description

Returns a list of workflow history entries for a specified workflow id.

**Note:** Stored workflow data expires after 60 days. Additionally, no data from before the 30th of October 2025 is available.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to access all, including project-scoped, workflows
 *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows
