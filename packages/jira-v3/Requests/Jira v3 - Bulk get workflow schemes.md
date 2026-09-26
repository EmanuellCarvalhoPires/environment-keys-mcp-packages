---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflowscheme/read"
category: "Workflow schemes"
writes_data: false
tool_note: "[[jira_bulk_get_workflow_schemes]]"
---
# Jira v3 - Bulk get workflow schemes

**Bulk get workflow schemes** — `POST /rest/api/3/workflowscheme/read`

- Run by the tool [[jira_bulk_get_workflow_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflowscheme/read
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
  "projectIds": [
    "10047",
    "10048"
  ],
  "workflowSchemeIds": [
    "3e59db0f-ed6c-47ce-8d50-80c0c4572677"
  ]
}
```

## Original description

Returns a list of workflow schemes by providing workflow scheme IDs or project IDs.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to access all, including project-scoped, workflow schemes
 *  *Administer projects* project permissions to access project-scoped workflow schemes
