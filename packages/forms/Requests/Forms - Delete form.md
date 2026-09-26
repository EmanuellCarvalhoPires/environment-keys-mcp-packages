---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-issue
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Forms]]"
app: "Forms"
method: DELETE
path: "/issue/{issueIdOrKey}/form/{formId}"
category: "Forms on Issue"
writes_data: true
---
# Forms - Delete form

**Delete form** — `DELETE /issue/{issueIdOrKey}/form/{formId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Delete form"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
DELETE https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/issue/{{param:issueIdOrKey}}/form/{{param:formId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Deletes a form from an issue.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Browse projects and Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
