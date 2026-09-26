---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-avatars
  - api/operation/update
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/project/{projectIdOrKey}/avatar"
category: "Project avatars"
writes_data: true
tool_note: "[[jira_set_project_avatar]]"
---
# Jira v3 - Set project avatar

**Set project avatar** — `PUT /rest/api/3/project/{projectIdOrKey}/avatar`

- Run by the tool [[jira_set_project_avatar]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/avatar
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The ID or (case-sensitive) key of the project.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "id": "10010"
}
```

## Original description

Sets the avatar displayed for a project.

Use [Load project avatar](#api-rest-api-3-project-projectIdOrKey-avatar2-post) to store avatars against the project, before using this operation to set the displayed avatar.

**[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
