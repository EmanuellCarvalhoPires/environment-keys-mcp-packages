---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-watches
  - api/operation/delete
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/user/watch/space/{spaceKey}"
category: "Content watches"
writes_data: true
tool_note: "[[confluence_v1_remove_space_watch]]"
---
# Confluence v1 - Remove space watch

**Remove space watch** — `DELETE /wiki/rest/api/user/watch/space/{spaceKey}`

- Run by the tool [[confluence_v1_remove_space_watch]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/user/watch/space/{{param:spaceKey}}?key={{param:key}}&username={{param:username}}&accountId={{param:accountId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to remove the watcher from.
- `key` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details.
- `username` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details.
- `accountId` (query, string, optional) — The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192.

## Original description

Removes a user as a watcher from a space. Choose the user by doing one of
the following:

- Specify a user via a query parameter: Use the `accountId` to identify the user.
- Do not specify a user: The currently logged-in user will be used.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Confluence Administrator' global permission or 'Space Administrator' permission for the relevant space if specifying a user, otherwise
permission to access the Confluence site ('Can use' global permission).
