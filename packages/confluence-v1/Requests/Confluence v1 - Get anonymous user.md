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
path: "/wiki/rest/api/user/anonymous"
category: "Users"
writes_data: false
tool_note: "[[confluence_v1_get_anonymous_user]]"
---
# Confluence v1 - Get anonymous user

**Get anonymous user** — `GET /wiki/rest/api/user/anonymous`

- Run by the tool [[confluence_v1_get_anonymous_user]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/user/anonymous?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the user to expand. - operations returns the operations that the user is allowed to do.

## Original description

Returns information about how anonymous users are represented, like the
profile picture and display name.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
