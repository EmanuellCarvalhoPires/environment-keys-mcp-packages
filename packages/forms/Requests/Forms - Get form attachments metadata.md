---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-customer-request
  - api/operation/list
  - api/effect/read
up: "[[MCP - Forms]]"
app: "Forms"
method: GET
path: "/request/{issueIdOrKey}/form/{formId}/attachment"
category: "Forms on Customer Request"
writes_data: false
---
# Forms - Get form attachments metadata

**Get form attachments metadata** — `GET /request/{issueIdOrKey}/form/{formId}/attachment`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get form attachments metadata"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/request/{{param:issueIdOrKey}}/form/{{param:formId}}/attachment
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Retrieve metadata for all attachments in a form on a request.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *View request* permission to view the customer request.
