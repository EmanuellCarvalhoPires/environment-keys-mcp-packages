---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/avatars
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/universal_avatar/type/{type}/owner/{entityId}"
category: "Avatars"
writes_data: false
tool_note: "[[jira_get_avatars]]"
---
# Jira v3 - Get avatars

**Get avatars** — `GET /rest/api/3/universal_avatar/type/{type}/owner/{entityId}`

- Run by the tool [[jira_get_avatars]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/universal_avatar/type/{{param:type}}/owner/{{param:entityId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `type` (path, string, required) — The avatar type.
- `entityId` (path, string, required) — The ID of the item the avatar is associated with.

## Original description

Returns the system and custom avatars for a project, issue type or priority.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  for custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
 *  for custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
 *  for system avatars, none.
 *  for priority avatars, none.
