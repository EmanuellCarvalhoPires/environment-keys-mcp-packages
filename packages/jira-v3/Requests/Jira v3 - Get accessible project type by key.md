---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-types
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/type/{projectTypeKey}/accessible"
category: "Project types"
writes_data: false
tool_note: "[[jira_get_accessible_project_type_by_key]]"
---
# Jira v3 - Get accessible project type by key

**Get accessible project type by key** — `GET /rest/api/3/project/type/{projectTypeKey}/accessible`

- Run by the tool [[jira_get_accessible_project_type_by_key]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/type/{{param:projectTypeKey}}/accessible
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectTypeKey` (path, string, required) — The key of the project type.

## Original description

Returns a [project type](https://confluence.atlassian.com/x/Var1Nw) if it is accessible to the user.

**[Permissions](#permissions) required:** Permission to access Jira.
