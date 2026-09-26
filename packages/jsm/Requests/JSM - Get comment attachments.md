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
path: "/rest/servicedeskapi/request/{issueIdOrKey}/comment/{commentId}/attachment"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_comment_attachments]]"
---
# JSM - Get comment attachments

**Get comment attachments** — `GET /rest/servicedeskapi/request/{issueIdOrKey}/comment/{commentId}/attachment`

- Run by the tool [[jsm_get_comment_attachments]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/comment/{{param:commentId}}/attachment?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request that contains the comment.
- `commentId` (path, string, required) — The ID of the comment.
- `start` (query, string, optional) — The starting index of the returned comments. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of comments to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns the attachments referenced in a comment.

**[Permissions](#permissions) required**: Permission to view the customer request.

**Response limitations**: Customers can only view public comments, and retrieve their attachments, on requests where they are the reporter or a participant whereas agents can see both internal and public comments.
