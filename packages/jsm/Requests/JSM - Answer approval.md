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
path: "/rest/servicedeskapi/request/{issueIdOrKey}/approval/{approvalId}"
category: "Request"
writes_data: true
tool_note: "[[jsm_answer_approval]]"
---
# JSM - Answer approval

**Answer approval** — `POST /rest/servicedeskapi/request/{issueIdOrKey}/approval/{approvalId}`

- Run by the tool [[jsm_answer_approval]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/approval/{{param:approvalId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request to be updated.
- `approvalId` (path, string, required) — The ID of the approval to be updated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "decision": "approve"
}
```

## Original description

This method enables a user to **Approve** or **Decline** an approval on a customer request. The approval is assumed to be owned by the user making the call.

**[Permissions](#permissions) required**: User is assigned to the approval request.
