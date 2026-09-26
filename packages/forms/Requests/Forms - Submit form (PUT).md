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
path: "/issue/{issueIdOrKey}/form/{formId}/action/submit"
category: "Forms on Issue"
writes_data: true
---
# Forms - Submit form (PUT)

**Submit form** — `PUT /issue/{issueIdOrKey}/form/{formId}/action/submit`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Submit form (PUT)"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
PUT https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/issue/{{param:issueIdOrKey}}/form/{{param:formId}}/action/submit
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Changes the status of a form on an issue to submitted.Depending on how the form is configured the form may either enter the submitted state or the locked state. Locked forms are considered to be submitted and locked and can only be reopened by project admins.We validate form answers before submission. This includes built-in rules and rules configured by Jira admins.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Browse projects and Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
