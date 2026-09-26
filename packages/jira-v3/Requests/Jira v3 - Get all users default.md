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
path: "/rest/api/3/users"
category: "Users"
writes_data: false
tool_note: "[[jira_get_all_users_default]]"
---
# Jira v3 - Get all users default

**Get all users default** — `GET /rest/api/3/users`

- Run by the tool [[jira_get_all_users_default]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/users?startAt={{param:startAt}}&maxResults={{param:maxResults}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return.
- `maxResults` (query, string, optional) — The maximum number of items to return (limited to 1000).
- `expand` (query, string, optional) — Query parameter expand.

## Original description

Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
