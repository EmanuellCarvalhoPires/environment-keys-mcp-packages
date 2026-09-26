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
path: "/rest/api/3/user/viewissue/search"
category: "User search"
writes_data: false
tool_note: "[[jira_find_users_with_browse_permission]]"
---
# Jira v3 - Find users with browse permission

**Find users with browse permission** — `GET /rest/api/3/user/viewissue/search`

- Run by the tool [[jira_find_users_with_browse_permission]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/viewissue/search?query={{param:query}}&username={{param:username}}&accountId={{param:accountId}}&issueKey={{param:issueKey}}&projectKey={{param:projectKey}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, optional) — A query string that is matched against user attributes, such as displayName and emailAddress, to find relevant users. The string can match the prefix of the attribute's value.
- `username` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `accountId` (query, string, optional) — A query string that is matched exactly against user accountId. Required, unless query is specified.
- `issueKey` (query, string, optional) — The issue key for the issue. Required, unless projectKey is specified.
- `projectKey` (query, string, optional) — The project key for the project (case sensitive). Required, unless issueKey is specified.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a list of users who fulfill these criteria:

 *  their user attributes match a search string.
 *  they have permission to browse issues.

Use this resource to find users who can browse:

 *  an issue, by providing the `issueKey`.
 *  any issue in a project, by providing the `projectKey`.

This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission to browse issues. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission to browse issues, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return empty search results.
