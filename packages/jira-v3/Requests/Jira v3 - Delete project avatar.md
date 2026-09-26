---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-avatars
  - api/operation/delete
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/project/{projectIdOrKey}/avatar/{id}"
category: "Project avatars"
writes_data: true
tool_note: "[[jira_delete_project_avatar]]"
---
# Jira v3 - Delete project avatar

**Delete project avatar** — `DELETE /rest/api/3/project/{projectIdOrKey}/avatar/{id}`

- Run by the tool [[jira_delete_project_avatar]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/avatar/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or (case-sensitive) key.
- `id` (path, string, required) — The ID of the avatar.

## Original description

Deletes a custom avatar from a project. Note that system avatars cannot be deleted.

**[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
