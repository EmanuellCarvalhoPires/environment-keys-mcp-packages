---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-issue
  - api/operation/list
  - api/effect/read
  - api/format/binary
up: "[[MCP - Forms]]"
app: "Forms"
method: GET
path: "/issue/{issueIdOrKey}/form/{formId}/format/xlsx"
category: "Forms on Issue"
writes_data: false
---
# Forms - Get form XLSX (GET)

**Get form XLSX** — `GET /issue/{issueIdOrKey}/form/{formId}/format/xlsx`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get form XLSX (GET)"`.
- **Format:** the response is binary (file/image); the plugin returns the body as text.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/issue/{{param:issueIdOrKey}}/form/{{param:formId}}/format/xlsx
Authorization: {{service.auth_token}}
Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Gets a single form on an issue as an XLSX file.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
