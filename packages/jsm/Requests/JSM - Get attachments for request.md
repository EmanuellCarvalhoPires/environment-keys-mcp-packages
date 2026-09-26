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
path: "/rest/servicedeskapi/request/{issueIdOrKey}/attachment"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_attachments_for_request]]"
---
# JSM - Get attachments for request

**Get attachments for request** — `GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment`

- Run by the tool [[jsm_get_attachments_for_request]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/attachment?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request from which the attachments will be listed.
- `start` (query, string, required) — The starting index of the returned attachment. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, required) — The maximum number of comments to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns all the attachments for a customer requests.

**[Permissions](#permissions) required**: Permission to view the customer request.

**Response limitations**: Customers will only get a list of public attachments.
