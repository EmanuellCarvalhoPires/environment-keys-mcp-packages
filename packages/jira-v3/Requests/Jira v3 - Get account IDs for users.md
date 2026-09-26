---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/user/bulk/migration"
category: "Users"
writes_data: false
tool_note: "[[jira_get_account_ids_for_users]]"
---
# Jira v3 - Get account IDs for users

**Get account IDs for users** — `GET /rest/api/3/user/bulk/migration`

- Run by the tool [[jira_get_account_ids_for_users]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/bulk/migration?startAt={{param:startAt}}&maxResults={{param:maxResults}}&username={{param:username}}&key={{param:key}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `username` (query, string, optional) — Username of a user. To specify multiple users, pass multiple copies of this parameter. For example, username=fred&username=barney. Required if key isn't provided. Cannot be provided if key is present.
- `key` (query, string, optional) — Key of a user. To specify multiple users, pass multiple copies of this parameter. For example, key=fred&key=barney. Required if username isn't provided. Cannot be provided if username is present.

## Original description

Returns the account IDs for the users specified in the `key` or `username` parameters. Note that multiple `key` or `username` parameters can be specified.

**[Permissions](#permissions) required:** Permission to access Jira.
