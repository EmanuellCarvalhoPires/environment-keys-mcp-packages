---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-issue
  - api/operation/action
  - api/effect/write
up: "[[MCP - Forms]]"
app: "Forms"
method: POST
path: "/issue/{sourceIssueIdOrKey}/form/copy/{targetIssueIdOrKey}"
category: "Forms on Issue"
writes_data: true
---
# Forms - Copy forms

**Copy forms** — `POST /issue/{sourceIssueIdOrKey}/form/copy/{targetIssueIdOrKey}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Copy forms"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
POST https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/issue/{{param:sourceIssueIdOrKey}}/form/copy/{{param:targetIssueIdOrKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `sourceIssueIdOrKey` (path, string, required) — The source issue key or ID
- `targetIssueIdOrKey` (path, string, required) — The target issue key or ID
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Copy forms from one issue to another.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Browse projects and Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
