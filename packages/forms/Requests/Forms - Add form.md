---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-issue
  - api/operation/create
  - api/effect/write
up: "[[MCP - Forms]]"
app: "Forms"
method: POST
path: "/issue/{issueIdOrKey}/form"
category: "Forms on Issue"
writes_data: true
---
# Forms - Add form

**Add form** — `POST /issue/{issueIdOrKey}/form`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Add form"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
POST https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/issue/{{param:issueIdOrKey}}/form
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds a form template to an issue.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Browse projects and Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
