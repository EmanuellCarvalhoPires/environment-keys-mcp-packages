---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/webhooks
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/hook_events"
category: "Webhooks"
writes_data: false
tool_note: "[[bitbucket_get_a_webhook_resource]]"
---
# Bitbucket - Get a webhook resource

**Get a webhook resource** — `GET /hook_events`

- Run by the tool [[bitbucket_get_a_webhook_resource]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/hook_events
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the webhook resource or subject types on which webhooks can be registered.
Each resource/subject type contains an `events` link that returns the paginated list of specific events each individual subject type can emit.
This endpoint is publicly accessible and does not require authentication or scopes.
