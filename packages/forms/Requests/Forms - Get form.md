---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-customer-request
  - api/operation/get
  - api/effect/read
up: "[[MCP - Forms]]"
app: "Forms"
method: GET
path: "/request/{issueIdOrKey}/form/{formId}"
category: "Forms on Customer Request"
writes_data: false
---
# Forms - Get form

**Get form** — `GET /request/{issueIdOrKey}/form/{formId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get form"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/request/{{param:issueIdOrKey}}/form/{{param:formId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Gets a single form on a request as a complete JSON object.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *View request* permission to view the customer request.

**Disclaimer:** This endpoint may return choice labels sourced from externally-configured data sources outside Atlassian's control. Treat these values as untrusted plain text and apply appropriate output encoding before rendering in any HTML context. See [Data connection choice labels](/cloud/forms/rest/#data-connection-choice-labels).
