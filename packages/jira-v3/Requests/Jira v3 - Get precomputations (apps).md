---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/jql-functions-apps
  - api/operation/search
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/jql/function/computation"
category: "JQL functions (apps)"
writes_data: false
---
# Jira v3 - Get precomputations (apps)

**Get precomputations (apps)** — `GET /rest/api/3/jql/function/computation`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get precomputations (apps)"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/jql/function/computation?functionKey={{param:functionKey}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}&orderBy={{param:orderBy}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `functionKey` (query, string, optional) — The function key in format: Forge: ari:cloud:ecosystem::extension/[App ID]/[Environment ID]/static/[Function key from manifest] Connect: [App key][Module key]
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `orderBy` (query, string, optional) — Order the results by a field: functionKey Sorts by the functionKey. used Sorts by the used timestamp. created Sorts by the created timestamp. updated Sorts by the updated timestamp.

## Original description

Returns the list of a function's precomputations along with information about when they were created, updated, and last used. Each precomputation has a `value` \- the JQL fragment to replace the custom function clause with.

**[Permissions](#permissions) required:** This API is only accessible to apps and apps can only inspect their own functions.

The new `read:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
