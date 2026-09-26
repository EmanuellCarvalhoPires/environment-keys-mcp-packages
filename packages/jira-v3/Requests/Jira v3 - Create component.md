---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/component"
category: "Project components"
writes_data: true
tool_note: "[[jira_create_component]]"
---
# Jira v3 - Create component

**Create component** — `POST /rest/api/3/component`

- Run by the tool [[jira_create_component]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/component
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "assigneeType": "PROJECT_LEAD",
  "description": "This is a Jira component",
  "isAssigneeTypeValid": false,
  "leadAccountId": "5b10a2844c20165700ede21g",
  "name": "Component 1",
  "project": "HSP"
}
```

## Original description

Creates a component. Use components to provide containers for issues within a project. Use components to provide containers for issues within a project.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the component is created or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
