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
path: "/rest/api/3/workflows"
category: "Workflows"
writes_data: false
tool_note: "[[jira_bulk_get_workflows]]"
---
# Jira v3 - Bulk get workflows

**Bulk get workflows** — `POST /rest/api/3/workflows`

- Run by the tool [[jira_bulk_get_workflows]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflows
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
  "projectAndIssueTypes": [],
  "workflowIds": [],
  "workflowNames": [
    "Workflow 1",
    "Workflow 2"
  ]
}
```

## Original description

Returns a list of workflows and related statuses by providing workflow names, workflow IDs, or project and issue types.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to access all, including project-scoped, workflows
 *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows
