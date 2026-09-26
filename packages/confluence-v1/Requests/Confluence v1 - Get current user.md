---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/users
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/user/current"
category: "Users"
writes_data: false
tool_note: "[[confluence_v1_get_current_user]]"
---
# Confluence v1 - Get current user

**Get current user** — `GET /wiki/rest/api/user/current`

- Run by the tool [[confluence_v1_get_current_user]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/user/current?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the user to expand. - operations returns the operations that the user is allowed to do.

## Original description

Returns the currently logged-in user. This includes information about
the user, like the display name, userKey, account ID, profile picture,
and more.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
