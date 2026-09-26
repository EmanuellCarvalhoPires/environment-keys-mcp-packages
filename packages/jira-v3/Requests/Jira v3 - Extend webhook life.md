---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/webhooks
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/webhook/refresh"
category: "Webhooks"
writes_data: true
tool_note: "[[jira_extend_webhook_life]]"
---
# Jira v3 - Extend webhook life

**Extend webhook life** — `PUT /rest/api/3/webhook/refresh`

- Run by the tool [[jira_extend_webhook_life]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/webhook/refresh
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "webhookIds": [
    10000,
    10001,
    10042
  ]
}
```

## Original description

Extends the life of webhook. Webhooks registered through the REST API expire after 30 days. Call this operation to keep them alive.

Unrecognized webhook IDs (those that are not found or belong to other apps) are ignored.

**[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.
