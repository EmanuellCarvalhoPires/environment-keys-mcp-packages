---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/user/assignable/multiProjectSearch"
category: "User search"
writes_data: false
tool_note: "[[jira_find_users_assignable_to_projects]]"
---
# Jira v3 - Find users assignable to projects

**Find users assignable to projects** — `GET /rest/api/3/user/assignable/multiProjectSearch`

- Run by the tool [[jira_find_users_assignable_to_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/assignable/multiProjectSearch?query={{param:query}}&username={{param:username}}&accountId={{param:accountId}}&projectKeys={{param:projectKeys}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, optional) — A query string that is matched against user attributes, such as displayName and emailAddress, to find relevant users. The string can match the prefix of the attribute's value.
- `username` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `accountId` (query, string, optional) — A query string that is matched exactly against user accountId. Required, unless query is specified.
- `projectKeys` (query, string, required) — A list of project keys (case sensitive). This parameter accepts a comma-separated list.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a list of users who can be assigned issues in one or more projects. The list may be restricted to users whose attributes match a string.

This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that can be assigned issues in the projects. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who can be assigned issues in the projects, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for each project specified in `projectKeys`.
