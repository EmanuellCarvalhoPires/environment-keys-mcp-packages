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
path: "/rest/api/3/user/bulk"
category: "Users"
writes_data: false
tool_note: "[[jira_bulk_get_users]]"
---
# Jira v3 - Bulk get users

**Bulk get users** — `GET /rest/api/3/user/bulk`

- Run by the tool [[jira_bulk_get_users]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/bulk?startAt={{param:startAt}}&maxResults={{param:maxResults}}&username={{param:username}}&key={{param:key}}&accountId={{param:accountId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `username` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details.
- `key` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details.
- `accountId` (query, string, required) — The account ID of a user. To specify multiple users, pass multiple accountId parameters. For example, accountId=5b10a2844c20165700ede21g&accountId=5b10ac8d82e05b22cc7d4ef5.

## Original description

Returns a [paginated](#pagination) list of the users specified by one or more account IDs.

**[Permissions](#permissions) required:** Permission to access Jira.
