---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflowscheme"
category: "Workflow schemes"
writes_data: true
tool_note: "[[jira_create_workflow_scheme]]"
---
# Jira v3 - Create workflow scheme

**Create workflow scheme** — `POST /rest/api/3/workflowscheme`

- Run by the tool [[jira_create_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflowscheme
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "defaultWorkflow": "jira",
  "description": "The description of the example workflow scheme.",
  "issueTypeMappings": {
    "10000": "scrum workflow",
    "10001": "builds workflow"
  },
  "name": "Example workflow scheme"
}
```

## Original description

Creates a workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
