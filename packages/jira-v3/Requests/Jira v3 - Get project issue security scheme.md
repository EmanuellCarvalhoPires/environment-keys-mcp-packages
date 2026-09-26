---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-permission-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme"
category: "Project permission schemes"
writes_data: false
tool_note: "[[jira_get_project_issue_security_scheme]]"
---
# Jira v3 - Get project issue security scheme

**Get project issue security scheme** — `GET /rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme`

- Run by the tool [[jira_get_project_issue_security_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectKeyOrId}}/issuesecuritylevelscheme
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectKeyOrId` (path, string, required) — The project ID or project key (case sensitive).

## Original description

Returns the [issue security scheme](https://confluence.atlassian.com/x/J4lKLg) associated with the project.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or the *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
