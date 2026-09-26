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
path: "/rest/api/3/user/search"
category: "User search"
writes_data: false
tool_note: "[[jira_find_users]]"
---
# Jira v3 - Find users

**Find users** — `GET /rest/api/3/user/search`

- Run by the tool [[jira_find_users]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/search?query={{param:query}}&username={{param:username}}&accountId={{param:accountId}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}&property={{param:property}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, optional) — A query string that is matched against user attributes ( displayName, and emailAddress) to find relevant users. The string can match the prefix of the attribute's value.
- `username` (query, string, optional) — Query parameter username.
- `accountId` (query, string, optional) — A query string that is matched exactly against a user accountId. Required, unless query or property is specified.
- `startAt` (query, string, optional) — The index of the first item to return in a page of filtered results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `property` (query, string, optional) — A query string used to search properties. Property keys are specified by path, so property keys containing dot (.) or equals (=) characters cannot be used.

## Original description

Returns a list of active users that match the search string and property.

This operation first applies a filter to match the search string and property, and then takes the filtered users in the range defined by `startAt` and `maxResults`, up to the thousandth user. To get all the users who match the search string and property, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

This operation can be accessed anonymously.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls or calls by users without the required permission return empty search results.
