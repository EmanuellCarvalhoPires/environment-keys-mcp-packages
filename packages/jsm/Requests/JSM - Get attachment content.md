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
path: "/rest/servicedeskapi/request/{issueIdOrKey}/attachment/{attachmentId}"
category: "Request"
writes_data: false
tool_note: "[[jsm_get_attachment_content]]"
---
# JSM - Get attachment content

**Get attachment content** — `GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment/{attachmentId}`

- Run by the tool [[jsm_get_attachment_content]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/request/{{param:issueIdOrKey}}/attachment/{{param:attachmentId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key for the customer request the attachment is associated with
- `attachmentId` (path, string, required) — The ID for the attachment

## Original description

Returns the contents of an attachment.

To return a thumbnail of the attachment, use [servicedeskapi/request/\{issueIdOrKey\}/attachment/\{attachmentId\}/thumbnail](./#api-rest-servicedeskapi-request-issueidorkey-attachment-attachmentid-thumbnail-get).

**[Permissions](#permissions) required:** For the issue containing the attachment:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
