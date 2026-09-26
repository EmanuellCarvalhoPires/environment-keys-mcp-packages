---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/avatars
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/avatar/{type}/system"
category: "Avatars"
writes_data: false
tool_note: "[[jira_get_system_avatars_by_type]]"
---
# Jira v3 - Get system avatars by type

**Get system avatars by type** — `GET /rest/api/3/avatar/{type}/system`

- Run by the tool [[jira_get_system_avatars_by_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/avatar/{{param:type}}/system
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `type` (path, string, required) — The avatar type.

## Original description

Returns a list of system avatar details by owner type, where the owner types are issue type, project, user or priority.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
