---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-issue
  - api/operation/get
  - api/effect/read
up: "[[MCP - Forms]]"
app: "Forms"
method: GET
path: "/issue/{issueIdOrKey}/form/{formId}"
category: "Forms on Issue"
writes_data: false
---
# Forms - Get form (GET)

**Get form** — `GET /issue/{issueIdOrKey}/form/{formId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get form (GET)"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/issue/{{param:issueIdOrKey}}/form/{{param:formId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Gets a single form on an issue as a complete JSON object.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

**Disclaimer:** This endpoint may return choice labels sourced from externally-configured data sources outside Atlassian's control. Treat these values as untrusted plain text and apply appropriate output encoding before rendering in any HTML context. See [Data connection choice labels](/cloud/forms/rest/#data-connection-choice-labels).
