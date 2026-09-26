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
path: "/rest/api/3/user/picker"
category: "User search"
writes_data: false
tool_note: "[[jira_find_users_for_picker]]"
---
# Jira v3 - Find users for picker

**Find users for picker** — `GET /rest/api/3/user/picker`

- Run by the tool [[jira_find_users_for_picker]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/picker?query={{param:query}}&maxResults={{param:maxResults}}&showAvatar={{param:showAvatar}}&exclude={{param:exclude}}&excludeAccountIds={{param:excludeAccountIds}}&avatarSize={{param:avatarSize}}&excludeConnectUsers={{param:excludeConnectUsers}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, required) — A query string that is matched against user attributes, such as displayName, and emailAddress, to find relevant users. The string can match the prefix of the attribute's value.
- `maxResults` (query, string, optional) — The maximum number of items to return. The total number of matched users is returned in total.
- `showAvatar` (query, string, optional) — Include the URI to the user's avatar.
- `exclude` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `excludeAccountIds` (query, string, optional) — A list of account IDs to exclude from the search results. This parameter accepts a comma-separated list. Multiple account IDs can also be provided using an ampersand-separated list.
- `avatarSize` (query, string, optional) — Query parameter avatarSize.
- `excludeConnectUsers` (query, string, optional) — Query parameter excludeConnectUsers.

## Original description

Returns a list of users whose attributes match the query term. The returned object includes the `html` field where the matched query term is highlighted with the HTML strong tag. A list of account IDs can be provided to exclude users from the results.

This operation takes the users in the range defined by `maxResults`, up to the thousandth user, and then returns only the users from that range that match the query term. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the query term, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return search results for an exact name match only.
