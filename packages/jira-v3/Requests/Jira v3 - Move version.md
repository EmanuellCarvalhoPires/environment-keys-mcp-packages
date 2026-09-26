---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/version/{id}/move"
category: "Project versions"
writes_data: true
tool_note: "[[jira_move_version]]"
---
# Jira v3 - Move version

**Move version** — `POST /rest/api/3/version/{id}/move`

- Run by the tool [[jira_move_version]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/version/{{param:id}}/move
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the version to be moved.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "after": "https://your-domain.atlassian.net/rest/api/~ver~/version/10000"
}
```

## Original description

Modifies the version's sequence within the project, which affects the display order of the versions in Jira.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.
