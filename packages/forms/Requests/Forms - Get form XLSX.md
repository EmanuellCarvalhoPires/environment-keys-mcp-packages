---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-customer-request
  - api/operation/list
  - api/effect/read
  - api/format/binary
up: "[[MCP - Forms]]"
app: "Forms"
method: GET
path: "/request/{issueIdOrKey}/form/{formId}/format/xlsx"
category: "Forms on Customer Request"
writes_data: false
---
# Forms - Get form XLSX

**Get form XLSX** — `GET /request/{issueIdOrKey}/form/{formId}/format/xlsx`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get form XLSX"`.
- **Format:** the response is binary (file/image); the plugin returns the body as text.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/request/{{param:issueIdOrKey}}/form/{{param:formId}}/format/xlsx
Authorization: {{service.auth_token}}
Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Gets a single form on a request as an XLSX file.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *View request* permission to view the customer request.
