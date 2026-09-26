---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user"
category: "Content restrictions"
writes_data: false
tool_note: "[[confluence_v1_get_content_restriction_status_for_user]]"
---
# Confluence v1 - Get content restriction status for user

**Get content restriction status for user** — `GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user`

- Run by the tool [[confluence_v1_get_content_restriction_status_for_user]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction/byOperation/{{param:operationKey}}/user?key={{param:key}}&username={{param:username}}&accountId={{param:accountId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that the restriction applies to.
- `operationKey` (path, string, required) — The operation that is restricted.
- `key` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details.
- `username` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details.
- `accountId` (query, string, optional) — The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192.

## Original description

Returns whether the specified content restriction applies to a user.
For example, if a page with `id=123` has a `read` restriction for a user with an account ID of
`384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192`, the following request will return `true`:

`/wiki/rest/api/content/123/restriction/byOperation/read/user?accountId=384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192`

Note that a response of `true` does not guarantee that the user can view the page, as it does not account for
account-inherited restrictions, space permissions, or even product access. For more
information, see [Confluence permissions](https://confluence.atlassian.com/x/_AozKw).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content.
