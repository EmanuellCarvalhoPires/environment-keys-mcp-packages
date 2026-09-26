---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/request/{issueIdOrKey}/notification"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_subscription_status]]"
---
# JSM - Get subscription status

**Get subscription status** — `GET /rest/servicedeskapi/request/{issueIdOrKey}/notification`

- Run by the tool [[jsm_get_subscription_status]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/notification
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request to be queried for subscription status.

## Original description

This method returns the notification subscription status of the user making the request. Use this method to determine if the user is subscribed to a customer request's notifications.

**[Permissions](#permissions) required**: Permission to view the customer request.
