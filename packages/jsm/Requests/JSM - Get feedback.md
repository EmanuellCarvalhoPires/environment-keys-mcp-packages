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
path: "/rest/servicedeskapi/request/{requestIdOrKey}/feedback"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_feedback]]"
---
# JSM - Get feedback

**Get feedback** — `GET /rest/servicedeskapi/request/{requestIdOrKey}/feedback`

- Run by the tool [[jsm_get_feedback]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:requestIdOrKey}}/feedback
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `requestIdOrKey` (path, string, required) — The id or the key of the request to post the feedback on

## Original description

This method retrieves a feedback of a request using it's `requestKey` or `requestId`

**[Permissions](#permissions) required**: User has view request permissions.
