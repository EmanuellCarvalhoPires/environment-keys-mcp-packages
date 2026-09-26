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
path: "/rest/servicedeskapi/request/{issueIdOrKey}/comment"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_request_comments]]"
---
# JSM - Get request comments

**Get request comments** — `GET /rest/servicedeskapi/request/{issueIdOrKey}/comment`

- Run by the tool [[jsm_get_request_comments]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/comment?public={{param:public}}&internal={{param:internal}}&expand={{param:expand}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request whose comments will be retrieved.
- `public` (query, string, optional) — Specifies whether to return public comments or not. Default: true.
- `internal` (query, string, optional) — Specifies whether to return internal comments or not. Default: true.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the comment to expand: attachment returns the attachment details, if any, for each comment.
- `start` (query, string, optional) — The starting index of the returned comments. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of comments to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns all comments on a customer request. No permissions error is provided if, for example, the user doesn't have access to the service desk or request, the method simply returns an empty response.

**[Permissions](#permissions) required**: Permission to view the customer request.

**Response limitations**: Customers are returned public comments only.
