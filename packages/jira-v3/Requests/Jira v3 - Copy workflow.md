---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflows/copy"
category: "Workflows"
writes_data: true
tool_note: "[[jira_copy_workflow]]"
---
# Jira v3 - Copy workflow

**Copy workflow** — `POST /rest/api/3/workflows/copy`

- Run by the tool [[jira_copy_workflow]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflows/copy
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
  "description": "A copy of the software workflow",
  "workflowId": "b9ff2384-d3b6-4d4e-9509-3ee19f607168",
  "workflowName": "Copy of Software workflow 1"
}
```

## Original description

Copies an existing workflow, and the statuses it uses, into a new workflow with the given name. The copy is created in the same scope as the workflow it is copied from. If no description is provided, the copy is created with an empty description.

Copying a workflow requires permission both to read the workflow being copied and to create the copy, which is created in the same scope as its source.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to copy all, including project-scoped, workflows
 *  To copy a project-scoped workflow, either the *Edit workflows* project permission, or both the *View (read-only) workflow* and *Administer projects* project permissions
