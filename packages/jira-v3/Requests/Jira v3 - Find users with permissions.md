---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-search
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/user/permission/search"
category: "User search"
writes_data: false
tool_note: "[[jira_find_users_with_permissions]]"
---
# Jira v3 - Find users with permissions

**Find users with permissions** — `GET /rest/api/3/user/permission/search`

- Run by the tool [[jira_find_users_with_permissions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/permission/search?query={{param:query}}&username={{param:username}}&accountId={{param:accountId}}&permissions={{param:permissions}}&issueKey={{param:issueKey}}&projectKey={{param:projectKey}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, optional) — A query string that is matched against user attributes, such as displayName and emailAddress, to find relevant users. The string can match the prefix of the attribute's value.
- `username` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `accountId` (query, string, optional) — A query string that is matched exactly against user accountId. Required, unless query is specified.
- `permissions` (query, string, required) — A comma separated list of permissions. Permissions can be specified as any: permission returned by Get all permissions. custom project permission added by Connect apps.
- `issueKey` (query, string, optional) — The issue key for the issue.
- `projectKey` (query, string, optional) — The project key for the project (case sensitive).
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a list of users who fulfill these criteria:

 *  their user attributes match a search string.
 *  they have a set of permissions for a project or issue.

If no search string is provided, a list of all users with the permissions is returned.

This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission for the project or issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission for the project or issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users for any project.
 *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project, to get users for that project.
