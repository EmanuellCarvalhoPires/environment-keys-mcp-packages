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
path: "/request/{issueIdOrKey}/form"
category: "Forms on Customer Request"
writes_data: false
---
# Forms - Get form index

**Get form index** — `GET /request/{issueIdOrKey}/form`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get form index"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/request/{{param:issueIdOrKey}}/form
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID

## Original description

Gets a list of forms on the customer request with basic metadata about them.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *View request* permission to view the customer request.
