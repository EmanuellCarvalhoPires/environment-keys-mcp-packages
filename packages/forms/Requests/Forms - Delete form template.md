---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-project
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Forms]]"
app: "Forms"
method: DELETE
path: "/project/{projectIdOrKey}/form/{formId}"
category: "Forms on Project"
writes_data: true
---
# Forms - Delete form template

**Delete form template** — `DELETE /project/{projectIdOrKey}/form/{formId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Delete form template"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
DELETE https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/project/{{param:projectIdOrKey}}/form/{{param:formId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Deletes a form on a project. This won't affect existing issues that already use this form, or any copies of this form in other projects.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Administer Jira* [project permission](https://confluence.atlassian.com/x/yodKLg).
