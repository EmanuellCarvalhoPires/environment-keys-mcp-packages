---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-project-associations
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/workflowscheme/project"
category: "Workflow scheme project associations"
writes_data: true
tool_note: "[[jira_assign_workflow_scheme_to_project]]"
---
# Jira v3 - Assign workflow scheme to project

**Assign workflow scheme to project** — `PUT /rest/api/3/workflowscheme/project`

- Run by the tool [[jira_assign_workflow_scheme_to_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/workflowscheme/project
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "projectId": "10001",
  "workflowSchemeId": "10032"
}
```

## Original description

Assigns a workflow scheme to a project. This operation is performed only when there are no issues in the project.

Workflow schemes can only be assigned to classic projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
