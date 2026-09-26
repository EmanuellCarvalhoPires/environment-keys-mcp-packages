---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/permissions
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/permissions/project"
category: "Permissions"
writes_data: false
tool_note: "[[jira_get_permitted_projects]]"
---
# Jira v3 - Get permitted projects

**Get permitted projects** — `POST /rest/api/3/permissions/project`

- Run by the tool [[jira_get_permitted_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/permissions/project
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Returns all the projects where the user is granted a list of project permissions.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
