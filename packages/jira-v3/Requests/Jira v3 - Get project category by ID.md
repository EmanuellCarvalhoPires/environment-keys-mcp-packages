---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-categories
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/projectCategory/{id}"
category: "Project categories"
writes_data: false
tool_note: "[[jira_get_project_category_by_id]]"
---
# Jira v3 - Get project category by ID

**Get project category by ID** — `GET /rest/api/3/projectCategory/{id}`

- Run by the tool [[jira_get_project_category_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/projectCategory/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the project category.

## Original description

Returns a project category.

**[Permissions](#permissions) required:** Permission to access Jira.
