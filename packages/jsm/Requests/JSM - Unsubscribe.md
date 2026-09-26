---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: DELETE
path: "/rest/servicedeskapi/request/{issueIdOrKey}/notification"
category: "Request"
writes_data: true
tool_note: "[[jsm_unsubscribe]]"
---
# JSM - Unsubscribe

**Unsubscribe** — `DELETE /rest/servicedeskapi/request/{issueIdOrKey}/notification`

- Run by the tool [[jsm_unsubscribe]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
DELETE {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/notification
Authorization: {{service.auth_token}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request to be unsubscribed from.

## Original description

This method unsubscribes the user from notifications from a customer request.

**[Permissions](#permissions) required**: Permission to view the customer request.
