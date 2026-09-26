---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/webhooks
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/webhook"
category: "Webhooks"
writes_data: true
tool_note: "[[jira_delete_webhooks_by_id]]"
---
# Jira v3 - Delete webhooks by ID

**Delete webhooks by ID** — `DELETE /rest/api/3/webhook`

- Run by the tool [[jira_delete_webhooks_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/webhook
Authorization: {{service.auth_token}}
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

Removes webhooks by ID. Only webhooks registered by the calling app are removed. If webhooks created by other apps are specified, they are ignored.

**[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.
