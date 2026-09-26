---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-email
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectId}/email"
category: "Project email"
writes_data: false
tool_note: "[[jira_get_project_s_sender_email]]"
---
# Jira v3 - Get project's sender email

**Get project's sender email** — `GET /rest/api/3/project/{projectId}/email`

- Run by the tool [[jira_get_project_s_sender_email]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectId}}/email
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectId` (path, string, required) — The project ID.

## Original description

Returns the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
