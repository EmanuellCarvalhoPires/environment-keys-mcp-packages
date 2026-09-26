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
path: "/rest/api/3/universal_avatar/view/type/{type}"
category: "Avatars"
writes_data: false
tool_note: "[[jira_get_avatar_image_by_type]]"
---
# Jira v3 - Get avatar image by type

**Get avatar image by type** — `GET /rest/api/3/universal_avatar/view/type/{type}`

- Run by the tool [[jira_get_avatar_image_by_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/universal_avatar/view/type/{{param:type}}?size={{param:size}}&format={{param:format}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `type` (path, string, required) — The icon type of the avatar.
- `size` (query, string, optional) — The size of the avatar image. If not provided the default size is returned.
- `format` (query, string, optional) — The format to return the avatar image in. If not provided the original content format is returned.

## Original description

Returns the default project, issue type or priority avatar image.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
