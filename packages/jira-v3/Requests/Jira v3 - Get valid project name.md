---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-key-and-name-validation
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/projectvalidate/validProjectName"
category: "Project key and name validation"
writes_data: false
tool_note: "[[jira_get_valid_project_name]]"
---
# Jira v3 - Get valid project name

**Get valid project name** — `GET /rest/api/3/projectvalidate/validProjectName`

- Run by the tool [[jira_get_valid_project_name]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/projectvalidate/validProjectName?name={{param:name}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `name` (query, string, required) — The project name.

## Original description

Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If the name is in use, this operation attempts to generate a valid project name based on the one supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404 response is returned.

**[Permissions](#permissions) required:** None.
