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
path: "/rest/api/3/user/assignable/search"
category: "User search"
writes_data: false
tool_note: "[[jira_find_users_assignable_to_issues]]"
---
# Jira v3 - Find users assignable to issues

**Find users assignable to issues** — `GET /rest/api/3/user/assignable/search`

- Run by the tool [[jira_find_users_assignable_to_issues]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/assignable/search?query={{param:query}}&sessionId={{param:sessionId}}&username={{param:username}}&accountId={{param:accountId}}&project={{param:project}}&issueKey={{param:issueKey}}&issueId={{param:issueId}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}&actionDescriptorId={{param:actionDescriptorId}}&recommend={{param:recommend}}&accountType={{param:accountType}}&appType={{param:appType}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, optional) — A query string that is matched against user attributes, such as displayName, and emailAddress, to find relevant users. The string can match the prefix of the attribute's value.
- `sessionId` (query, string, optional) — The sessionId of this request. SessionId is the same until the assignee is set.
- `username` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `accountId` (query, string, optional) — A query string that is matched exactly against user accountId. Required, unless query is specified.
- `project` (query, string, optional) — The project ID or project key (case sensitive). Required, unless issueKey or issueId is specified.
- `issueKey` (query, string, optional) — The key of the issue. Required, unless issueId or project is specified.
- `issueId` (query, string, optional) — The ID of the issue. Required, unless issueKey or project is specified.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return. This operation may return less than the maximum number of items even if more are available.
- `actionDescriptorId` (query, string, optional) — The ID of the transition.
- `recommend` (query, string, optional) — Query parameter recommend.
- `accountType` (query, string, optional) — Query parameter accountType.
- `appType` (query, string, optional) — Query parameter appType.

## Original description

Returns a list of users that can be assigned to an issue. Use this operation to find the list of users who can be assigned to:

 *  a new issue, by providing the `projectKeyOrId`.
 *  an updated issue, by providing the `issueKey` or `issueId`.
 *  to an issue during a transition (workflow action), by providing the `issueKey` or `issueId` and the transition id in `actionDescriptorId`. You can obtain the IDs of an issue's valid transitions using the `transitions` option in the `expand` parameter of [ Get issue](#api-rest-api-3-issue-issueIdOrKey-get).

In all these cases, you can pass an account ID to determine if a user can be assigned to an issue. The user is returned in the response if they can be assigned to the issue or issue transition.

This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that can be assigned the issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who can be assigned the issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Assign issues* [project permission](https://confluence.atlassian.com/x/yodKLg)
