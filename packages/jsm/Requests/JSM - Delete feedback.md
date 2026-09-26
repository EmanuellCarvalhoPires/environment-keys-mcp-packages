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
path: "/rest/servicedeskapi/request/{requestIdOrKey}/feedback"
category: "Request"
writes_data: true
tool_note: "[[jsm_delete_feedback]]"
---
# JSM - Delete feedback

**Delete feedback** — `DELETE /rest/servicedeskapi/request/{requestIdOrKey}/feedback`

- Run by the tool [[jsm_delete_feedback]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
DELETE {{service.url}}/rest/servicedeskapi/request/{{param:requestIdOrKey}}/feedback
Authorization: {{service.auth_token}}
```

## Parameters

- `requestIdOrKey` (path, string, required) — The id or the key of the request to post the feedback on

## Original description

This method deletes the feedback of request using it's `requestKey` or `requestId`

**[Permissions](#permissions) required**: User must be the reporter or an Atlassian Connect app.
