---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/request/{requestIdOrKey}/feedback"
category: "Request"
writes_data: true
tool_note: "[[jsm_post_feedback]]"
---
# JSM - Post feedback

**Post feedback** — `POST /rest/servicedeskapi/request/{requestIdOrKey}/feedback`

- Run by the tool [[jsm_post_feedback]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/request/{{param:requestIdOrKey}}/feedback
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `requestIdOrKey` (path, string, required) — The id or the key of the request to post the feedback on
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "comment": {
    "body": "Great work!"
  },
  "rating": 4,
  "type": "csat"
}
```

## Original description

This method adds a feedback on an request using it's `requestKey` or `requestId`

**[Permissions](#permissions) required**: User must be the reporter or an Atlassian Connect app.
