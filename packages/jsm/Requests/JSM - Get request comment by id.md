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
path: "/rest/servicedeskapi/request/{issueIdOrKey}/comment/{commentId}"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_request_comment_by_id]]"
---
# JSM - Get request comment by id

**Get request comment by id** — `GET /rest/servicedeskapi/request/{issueIdOrKey}/comment/{commentId}`

- Run by the tool [[jsm_get_request_comment_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/comment/{{param:commentId}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request that contains the comment.
- `commentId` (path, string, required) — The ID of the comment to retrieve.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the comment to expand: attachment returns the attachment details, if any, for the comment.

## Original description

This method returns details of a customer request's comment.

**[Permissions](#permissions) required**: Permission to view the customer request.

**Response limitations**: Customers can only view public comments on requests where they are the reporter or a participant whereas agents can see both internal and public comments.
