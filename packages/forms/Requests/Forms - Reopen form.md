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
path: "/issue/{issueIdOrKey}/form/{formId}/action/reopen"
category: "Forms on Issue"
writes_data: true
---
# Forms - Reopen form

**Reopen form** — `PUT /issue/{issueIdOrKey}/form/{formId}/action/reopen`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Reopen form"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
PUT https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/issue/{{param:issueIdOrKey}}/form/{{param:formId}}/action/reopen
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Changes the status of a submitted form on an issue to open to enable editing. Locked forms can only be reopened by a project admin.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Browse projects and Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

 *  *Administer Jira* [project permission](https://confluence.atlassian.com/x/x4dKLg) if the form is locked.
