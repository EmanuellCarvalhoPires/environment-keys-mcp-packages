---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-issue
  - api/operation/update
  - api/effect/write
up: "[[MCP - Forms]]"
app: "Forms"
method: PUT
path: "/issue/{issueIdOrKey}/form/{formId}"
category: "Forms on Issue"
writes_data: true
---
# Forms - Save form answers (PUT)

**Save form answers** — `PUT /issue/{issueIdOrKey}/form/{formId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Save form answers (PUT)"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
PUT https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/issue/{{param:issueIdOrKey}}/form/{{param:formId}}
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

Saves form answers on an issue.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Browse projects and Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
