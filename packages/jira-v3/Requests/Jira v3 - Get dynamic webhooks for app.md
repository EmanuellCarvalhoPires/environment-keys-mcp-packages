---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/webhooks
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/webhook"
category: "Webhooks"
writes_data: false
tool_note: "[[jira_get_dynamic_webhooks_for_app]]"
---
# Jira v3 - Get dynamic webhooks for app

**Get dynamic webhooks for app** — `GET /rest/api/3/webhook`

- Run by the tool [[jira_get_dynamic_webhooks_for_app]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/webhook?startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a [paginated](#pagination) list of the webhooks registered by the calling app.

**[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.
