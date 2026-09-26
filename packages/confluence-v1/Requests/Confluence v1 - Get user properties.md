---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user-properties
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/user/{userId}/property"
category: "User properties"
writes_data: false
tool_note: "[[confluence_v1_get_user_properties]]"
---
# Confluence v1 - Get user properties

**Get user properties** — `GET /wiki/rest/api/user/{userId}/property`

- Run by the tool [[confluence_v1_get_user_properties]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/user/{{param:userId}}/property?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `userId` (path, string, required) — The account ID of the user to be queried for its properties.
- `start` (query, string, optional) — The starting index of the returned properties.
- `limit` (query, string, optional) — The maximum number of properties to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns the properties for a user as list of property keys. For more information
about user properties, see [Confluence entity properties](https://developer.atlassian.com/cloud/confluence/confluence-entity-properties/).
`Note`, these properties stored against a user are on a Confluence site level and not space/content level.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
