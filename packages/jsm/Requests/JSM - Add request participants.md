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
path: "/rest/servicedeskapi/request/{issueIdOrKey}/participant"
category: "Request"
writes_data: true
tool_note: "[[jsm_add_request_participants]]"
---
# JSM - Add request participants

**Add request participants** — `POST /rest/servicedeskapi/request/{issueIdOrKey}/participant`

- Run by the tool [[jsm_add_request_participants]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/participant
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request to have participants added.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "accountIds": [],
  "usernames": [
    "qm:a713c8ea-1075-4e30-9d96-891a7d181739:5ad6d3581db05e2a66fa80b",
    "qm:a713c8ea-1075-4e30-9d96-891a7d181739:5ad6d3a01db05e2a66fa80bd",
    "qm:a713c8ea-1075-4e30-9d96-891a7d181739:5ad6d69abfa3980ce712caae"
  ]
}
```

## Original description

This method adds participants to a customer request.

**[Permissions](#permissions) required**: Permission to manage participants on the customer request.

Note, participants can be added when creating a customer request using the [request](#api-request-post) resource, by defining the participants in the `requestParticipants` field.
