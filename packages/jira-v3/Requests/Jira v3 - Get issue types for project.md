---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuetype/project"
category: "Issue types"
writes_data: false
tool_note: "[[jira_get_issue_types_for_project]]"
---
# Jira v3 - Get issue types for project

**Get issue types for project** — `GET /rest/api/3/issuetype/project`

- Run by the tool [[jira_get_issue_types_for_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuetype/project?projectId={{param:projectId}}&level={{param:level}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectId` (query, string, required) — The ID of the project.
- `level` (query, string, optional) — The level of the issue type to filter by. Use: -1 for Subtask. 0 for Base. 1 for Epic.

## Original description

Returns issue types for a project.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
