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
path: "/rest/servicedeskapi/request/{issueIdOrKey}/comment"
category: "Request"
writes_data: true
tool_note: "[[jsm_create_request_comment]]"
---
# JSM - Create request comment

**Create request comment** — `POST /rest/servicedeskapi/request/{issueIdOrKey}/comment`

- Run by the tool [[jsm_create_request_comment]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/comment
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request to which the comment will be added.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "body": "Hello there",
  "public": true
}
```

## Original description

This method creates a public or private (internal) comment on a customer request, with the comment visibility set by `public`. The user recorded as the author of the comment.

**[Permissions](#permissions) required**: User has Add Comments permission.

**Request limitations**: Customers can set comments to public visibility only.
