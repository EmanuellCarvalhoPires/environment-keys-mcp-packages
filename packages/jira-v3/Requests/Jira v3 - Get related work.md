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
path: "/rest/api/3/version/{id}/relatedwork"
category: "Project versions"
writes_data: false
tool_note: "[[jira_get_related_work]]"
---
# Jira v3 - Get related work

**Get related work** — `GET /rest/api/3/version/{id}/relatedwork`

- Run by the tool [[jira_get_related_work]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/version/{{param:id}}/relatedwork
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the version.

## Original description

Returns related work items for the given version id.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.
