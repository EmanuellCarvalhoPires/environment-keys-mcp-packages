---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-categories
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/projectCategory"
category: "Project categories"
writes_data: true
tool_note: "[[jira_create_project_category]]"
---
# Jira v3 - Create project category

**Create project category** — `POST /rest/api/3/projectCategory`

- Run by the tool [[jira_create_project_category]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/projectCategory
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Created Project Category",
  "name": "CREATED"
}
```

## Original description

Creates a project category.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
