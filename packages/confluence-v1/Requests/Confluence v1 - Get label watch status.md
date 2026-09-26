---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-watches
  - api/operation/get
  - api/effect/read
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/user/watch/label/{labelName}"
category: "Content watches"
writes_data: false
tool_note: "[[confluence_v1_get_label_watch_status]]"
---
# Confluence v1 - Get label watch status

**Get label watch status** — `GET /wiki/rest/api/user/watch/label/{labelName}`

- Run by the tool [[confluence_v1_get_label_watch_status]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/user/watch/label/{{param:labelName}}?key={{param:key}}&username={{param:username}}&accountId={{param:accountId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `labelName` (path, string, required) — The name of the label to be queried for whether the specified user is watching it.
- `key` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details.
- `username` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details.
- `accountId` (query, string, optional) — The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192.

## Original description

Returns whether a user is watching a label. Choose the user by doing one
of the following:

- Specify a user via a query parameter: Use the `accountId` to identify the user.
- Do not specify a user: The currently logged-in user will be used.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Confluence Administrator' global permission if specifying a user, otherwise
permission to access the Confluence site ('Can use' global permission).
