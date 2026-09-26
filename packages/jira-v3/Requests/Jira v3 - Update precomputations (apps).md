---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/jql-functions-apps
  - api/operation/action
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/jql/function/computation"
category: "JQL functions (apps)"
writes_data: true
---
# Jira v3 - Update precomputations (apps)

**Update precomputations (apps)** — `POST /rest/api/3/jql/function/computation`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Update precomputations (apps)"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/jql/function/computation?skipNotFoundPrecomputations={{param:skipNotFoundPrecomputations}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `skipNotFoundPrecomputations` (query, string, optional) — Query parameter skipNotFoundPrecomputations.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "values": [
    {
      "id": "f2ef228b-367f-4c6b-bd9d-0d0e96b5bd7b",
      "value": "issue in (TEST-1, TEST-2, TEST-3)"
    },
    {
      "error": "Error message to be displayed to the user",
      "id": "2a854f11-d0e1-4260-aea8-64a562a7062a"
    }
  ]
}
```

## Original description

Update the precomputation value of a function created by a Forge/Connect app.

**[Permissions](#permissions) required:** An API for apps to update their own precomputations.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
