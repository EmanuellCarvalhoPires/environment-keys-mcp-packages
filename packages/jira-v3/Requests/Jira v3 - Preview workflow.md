---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflows/preview"
category: "Workflows"
writes_data: true
tool_note: "[[jira_preview_workflow]]"
---
# Jira v3 - Preview workflow

**Preview workflow** — `POST /rest/api/3/workflows/preview`

- Run by the tool [[jira_preview_workflow]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflows/preview
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
  "issueTypeIds": [],
  "projectId": "10011",
  "workflowIds": [
    "3215e5cd-f09f-4c8a-921b-dca92bd1e9aa",
    "5f485405-a237-40e5-aeea-ad2c206cff95"
  ],
  "workflowNames": []
}
```

## Original description

Returns a requested workflow within a given project. The response provides a read-only preview of the workflow, omitting full configuration details.

**[Permissions](#permissions) required:**

 *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions
