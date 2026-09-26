---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/ui-modifications-apps
  - api/operation/list
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/uiModifications"
category: "UI modifications (apps)"
writes_data: false
---
# Jira v3 - Get UI modifications

**Get UI modifications** — `GET /rest/api/3/uiModifications`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get UI modifications"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/uiModifications?startAt={{param:startAt}}&maxResults={{param:maxResults}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include: data Returns UI modification data.

## Original description

Gets UI modifications. UI modifications can only be retrieved by Forge apps.

**[Permissions](#permissions) required:** None.

The new `read:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
