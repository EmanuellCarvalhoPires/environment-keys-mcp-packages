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
path: "/rest/servicedeskapi/request/{issueIdOrKey}/attachment"
category: "Request"
writes_data: true
tool_note: "[[jsm_create_comment_with_attachment]]"
---
# JSM - Create comment with attachment

**Create comment with attachment** — `POST /rest/servicedeskapi/request/{issueIdOrKey}/attachment`

- Run by the tool [[jsm_create_comment_with_attachment]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/attachment
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the customer request to which the attachment will be added.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "additionalComment": {
    "body": "Please find the screenshot and the log file attached."
  },
  "public": true,
  "temporaryAttachmentIds": [
    "temp910441317820424274",
    "temp3600755449679003114"
  ]
}
```

## Original description

This method creates a comment on a customer request using one or more attachment files (uploaded using [servicedeskapi/servicedesk/\{serviceDeskId\}/attachTemporaryFile](https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-servicedesk/#api-rest-servicedeskapi-servicedesk-servicedeskid-attachtemporaryfile-post)), with the visibility set by `public`. See

 *  GET [servicedeskapi/request/\{issueIdOrKey\}/attachment](./#api-rest-servicedeskapi-request-issueidorkey-attachment-get)
 *  GET [servicedeskapi/request/\{issueIdOrKey\}/comment/\{commentId\}/attachment](./#api-rest-servicedeskapi-request-issueidorkey-comment-commentid-attachment-get)

**[Permissions](#permissions) required**: Permission to add an attachment.

**Request limitations**: Customers can set public visibility only.
