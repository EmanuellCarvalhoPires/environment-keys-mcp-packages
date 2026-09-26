---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user-properties
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/user/{userId}/property/{key}"
category: "User properties"
writes_data: true
tool_note: "[[confluence_v1_delete_user_property]]"
---
# Confluence v1 - Delete user property

**Delete user property** — `DELETE /wiki/rest/api/user/{userId}/property/{key}`

- Run by the tool [[confluence_v1_delete_user_property]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/user/{{param:userId}}/property/{{param:key}}
Authorization: {{service.auth_token}}
```

## Parameters

- `userId` (path, string, required) — The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192
- `key` (path, string, required) — The key of the user property.

## Original description

Deletes a property for the given user.
For more information about user properties, see
[Confluence entity properties](https://developer.atlassian.com/cloud/confluence/confluence-entity-properties/).
`Note`, these properties stored against a user are on a Confluence site level and not space/content level.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
