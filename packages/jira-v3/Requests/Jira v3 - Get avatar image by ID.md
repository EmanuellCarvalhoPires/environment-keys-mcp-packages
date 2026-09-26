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
path: "/rest/api/3/universal_avatar/view/type/{type}/avatar/{id}"
category: "Avatars"
writes_data: false
tool_note: "[[jira_get_avatar_image_by_id]]"
---
# Jira v3 - Get avatar image by ID

**Get avatar image by ID** — `GET /rest/api/3/universal_avatar/view/type/{type}/avatar/{id}`

- Run by the tool [[jira_get_avatar_image_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/universal_avatar/view/type/{{param:type}}/avatar/{{param:id}}?size={{param:size}}&format={{param:format}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `type` (path, string, required) — The icon type of the avatar.
- `id` (path, string, required) — The ID of the avatar.
- `size` (query, string, optional) — The size of the avatar image. If not provided the default size is returned.
- `format` (query, string, optional) — The format to return the avatar image in. If not provided the original content format is returned.

## Original description

Returns a project, issue type or priority avatar image by ID.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  For system avatars, none.
 *  For custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
 *  For custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
 *  For priority avatars, none.
