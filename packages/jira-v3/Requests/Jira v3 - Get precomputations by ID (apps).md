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
method: POST
path: "/rest/api/3/jql/function/computation/search"
category: "JQL functions (apps)"
writes_data: false
---
# Jira v3 - Get precomputations by ID (apps)

**Get precomputations by ID (apps)** — `POST /rest/api/3/jql/function/computation/search`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get precomputations by ID (apps)"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/jql/function/computation/search?orderBy={{param:orderBy}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `orderBy` (query, string, optional) — Order the results by a field: functionKey Sorts by the functionKey. used Sorts by the used timestamp. created Sorts by the created timestamp. updated Sorts by the updated timestamp.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "precomputationIDs": [
    "f2ef228b-367f-4c6b-bd9d-0d0e96b5bd7b",
    "2a854f11-d0e1-4260-aea8-64a562a7062a"
  ]
}
```

## Original description

Returns function precomputations by IDs, along with information about when they were created, updated, and last used. Each precomputation has a `value` \- the JQL fragment to replace the custom function clause with.

**[Permissions](#permissions) required:** This API is only accessible to apps and apps can only inspect their own functions.

The new `read:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
