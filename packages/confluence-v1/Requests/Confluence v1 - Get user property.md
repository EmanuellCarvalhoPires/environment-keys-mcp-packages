---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user-properties
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/user/{userId}/property/{key}"
category: "User properties"
writes_data: false
tool_note: "[[confluence_v1_get_user_property]]"
---
# Confluence v1 - Get user property

**Get user property** — `GET /wiki/rest/api/user/{userId}/property/{key}`

- Run by the tool [[confluence_v1_get_user_property]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/user/{{param:userId}}/property/{{param:key}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `userId` (path, string, required) — The account ID of the user to be queried for its properties.
- `key` (path, string, required) — The key of the user property.

## Original description

Returns the property corresponding to `key` for a user. For more information
about user properties, see [Confluence entity properties](https://developer.atlassian.com/cloud/confluence/confluence-entity-properties/).
`Note`, these properties stored against a user are on a Confluence site level and not space/content level.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
