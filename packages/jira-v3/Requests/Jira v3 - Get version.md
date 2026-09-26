---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/version/{id}"
category: "Project versions"
writes_data: false
tool_note: "[[jira_get_version]]"
---
# Jira v3 - Get version

**Get version** — `GET /rest/api/3/version/{id}`

- Run by the tool [[jira_get_version]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/version/{{param:id}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the version.
- `expand` (query, string, optional) — Use expand to include additional information about version in the response. This parameter accepts a comma-separated list.

## Original description

Returns a project version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.
