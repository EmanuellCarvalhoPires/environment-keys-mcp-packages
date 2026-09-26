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
path: "/request/{issueIdOrKey}/form/{formId}/externaldata"
category: "Forms on Customer Request"
writes_data: false
---
# Forms - Get external form data

**Get external form data** — `GET /request/{issueIdOrKey}/form/{formId}/externaldata`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get external form data"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/request/{{param:issueIdOrKey}}/form/{{param:formId}}/externaldata
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Get all external form data for questions and answers on a form added to a request. Forms can be linked to external sources including Jira fields and data connections, with this API returning the latest responses on these linked fields.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *View request* permission to view the customer request.

**Disclaimer:** This endpoint may return choice labels sourced from externally-configured data sources outside Atlassian's control. Treat these values as untrusted plain text and apply appropriate output encoding before rendering in any HTML context. See [Data connection choice labels](/cloud/forms/rest/#data-connection-choice-labels).
