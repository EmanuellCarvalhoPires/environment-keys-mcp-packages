---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-permission-schemes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectKeyOrId}/securitylevel"
category: "Project permission schemes"
writes_data: false
tool_note: "[[jira_get_project_issue_security_levels]]"
---
# Jira v3 - Get project issue security levels

**Get project issue security levels** — `GET /rest/api/3/project/{projectKeyOrId}/securitylevel`

- Run by the tool [[jira_get_project_issue_security_levels]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectKeyOrId}}/securitylevel
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectKeyOrId` (path, string, required) — The project ID or project key (case sensitive).

## Original description

Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that the user has access to.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security levels are only returned for authenticated user with *Set Issue Security* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project.
