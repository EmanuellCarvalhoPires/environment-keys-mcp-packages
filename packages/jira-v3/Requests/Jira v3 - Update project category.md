---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-categories
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/projectCategory/{id}"
category: "Project categories"
writes_data: true
tool_note: "[[jira_update_project_category]]"
---
# Jira v3 - Update project category

**Update project category** — `PUT /rest/api/3/projectCategory/{id}`

- Run by the tool [[jira_update_project_category]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/projectCategory/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Updated Project Category",
  "name": "UPDATED"
}
```

## Original description

Updates a project category.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
