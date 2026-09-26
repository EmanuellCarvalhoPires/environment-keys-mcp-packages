---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-customer-request
  - api/operation/update
  - api/effect/write
up: "[[MCP - Forms]]"
app: "Forms"
method: PUT
path: "/request/{issueIdOrKey}/form/{formId}"
category: "Forms on Customer Request"
writes_data: true
---
# Forms - Save form answers

**Save form answers** — `PUT /request/{issueIdOrKey}/form/{formId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Save form answers"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
PUT https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/request/{{param:issueIdOrKey}}/form/{{param:formId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Saves form answers on a request.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *Edit request* permission to edit the customer request.
