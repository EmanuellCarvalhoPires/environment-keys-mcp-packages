---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/request/{issueIdOrKey}/transition"
category: "Request"
writes_data: true
tool_note: "[[jsm_perform_customer_transition]]"
---
# JSM - Perform customer transition

**Perform customer transition** — `POST /rest/servicedeskapi/request/{issueIdOrKey}/transition`

- Run by the tool [[jsm_perform_customer_transition]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/transition
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — ID or key of the issue to transition
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "additionalComment": {
    "body": "I have fixed the problem."
  },
  "id": "1"
}
```

## Original description

This method performs a customer transition for a given request and transition. An optional comment can be included to provide a reason for the transition.

**[Permissions](#permissions) required**: The user must be able to view the request and have the Transition Issues permission. If a comment is passed the user must have the Add Comments permission.
