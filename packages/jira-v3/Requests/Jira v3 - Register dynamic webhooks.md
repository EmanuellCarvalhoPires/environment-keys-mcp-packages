---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/webhooks
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/webhook"
category: "Webhooks"
writes_data: true
tool_note: "[[jira_register_dynamic_webhooks]]"
---
# Jira v3 - Register dynamic webhooks

**Register dynamic webhooks** — `POST /rest/api/3/webhook`

- Run by the tool [[jira_register_dynamic_webhooks]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/webhook
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
  "url": "https://your-app.example.com/webhook-received",
  "webhooks": [
    {
      "events": [
        "jira:issue_created",
        "jira:issue_updated"
      ],
      "fieldIdsFilter": [
        "summary",
        "customfield_10029"
      ],
      "jqlFilter": "project = PROJ"
    },
    {
      "events": [
        "jira:issue_deleted"
      ],
      "jqlFilter": "project IN (PROJ, EXP) AND status = done"
    },
    {
      "events": [
        "issue_property_set"
      ],
      "issuePropertyKeysFilter": [
        "my-issue-property-key"
      ],
      "jqlFilter": "project = PROJ"
    }
  ]
}
```

## Original description

Registers webhooks.

**NOTE:** for non-public OAuth apps, webhooks are delivered only if there is a match between the app owner and the user who registered a dynamic webhook.

**[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.
