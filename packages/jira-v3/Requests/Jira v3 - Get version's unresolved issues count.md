---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/version/{id}/unresolvedIssueCount"
category: "Project versions"
writes_data: false
tool_note: "[[jira_get_version_s_unresolved_issues_count]]"
---
# Jira v3 - Get version's unresolved issues count

**Get version's unresolved issues count** — `GET /rest/api/3/version/{id}/unresolvedIssueCount`

- Run by the tool [[jira_get_version_s_unresolved_issues_count]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/version/{{param:id}}/unresolvedIssueCount
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the version.

## Original description

Returns counts of the issues and unresolved issues for the project version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.
