---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/request/{issueIdOrKey}/approval/{approvalId}"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_approval_by_id]]"
---
# JSM - Get approval by id

**Get approval by id** — `GET /rest/servicedeskapi/request/{issueIdOrKey}/approval/{approvalId}`

- Run by the tool [[jsm_get_approval_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/approval/{{param:approvalId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request the approval is on.
- `approvalId` (path, string, required) — The ID of the approval to be returned.

## Original description

This method returns an approval. Use this method to determine the status of an approval and the list of approvers.

**[Permissions](#permissions) required**: Permission to view the customer request.
