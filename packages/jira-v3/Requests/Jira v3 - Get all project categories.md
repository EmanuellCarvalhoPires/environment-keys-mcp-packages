---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-categories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/projectCategory"
category: "Project categories"
writes_data: false
tool_note: "[[jira_get_all_project_categories]]"
---
# Jira v3 - Get all project categories

**Get all project categories** — `GET /rest/api/3/projectCategory`

- Run by the tool [[jira_get_all_project_categories]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/projectCategory
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all project categories.

**[Permissions](#permissions) required:** Permission to access Jira.
