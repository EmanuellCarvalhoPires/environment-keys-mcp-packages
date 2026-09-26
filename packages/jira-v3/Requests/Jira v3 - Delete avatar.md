---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/avatars
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}"
category: "Avatars"
writes_data: true
tool_note: "[[jira_delete_avatar]]"
---
# Jira v3 - Delete avatar

**Delete avatar** — `DELETE /rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}`

- Run by the tool [[jira_delete_avatar]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/universal_avatar/type/{{param:type}}/owner/{{param:owningObjectId}}/avatar/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `type` (path, string, required) — The avatar type.
- `owningObjectId` (path, string, required) — The ID of the item the avatar is associated with.
- `id` (path, string, required) — The ID of the avatar.

## Original description

Deletes an avatar from a project, issue type or priority.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
