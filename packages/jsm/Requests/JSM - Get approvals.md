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
path: "/rest/servicedeskapi/request/{issueIdOrKey}/approval"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_approvals]]"
---
# JSM - Get approvals

**Get approvals** — `GET /rest/servicedeskapi/request/{issueIdOrKey}/approval`

- Run by the tool [[jsm_get_approvals]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/approval?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request to be queried for its approvals.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of approvals to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns all approvals on a customer request.

**[Permissions](#permissions) required**: Permission to view the customer request.
