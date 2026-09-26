---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: PUT
path: "/rest/servicedeskapi/request/{issueIdOrKey}/notification"
category: "Request"
writes_data: true
tool_note: "[[jsm_subscribe]]"
---
# JSM - Subscribe

**Subscribe** — `PUT /rest/servicedeskapi/request/{issueIdOrKey}/notification`

- Run by the tool [[jsm_subscribe]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
PUT {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/notification
Authorization: {{service.auth_token}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request to be subscribed to.

## Original description

This method subscribes the user to receiving notifications from a customer request.

**[Permissions](#permissions) required**: Permission to view the customer request.
