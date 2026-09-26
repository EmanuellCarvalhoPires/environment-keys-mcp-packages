---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-project
  - api/operation/get
  - api/effect/read
up: "[[MCP - Forms]]"
app: "Forms"
method: GET
path: "/project/{projectIdOrKey}/form/{formId}"
category: "Forms on Project"
writes_data: false
---
# Forms - Get form template

**Get form template** — `GET /project/{projectIdOrKey}/form/{formId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get form template"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/project/{{param:projectIdOrKey}}/form/{{param:formId}}?requestLanguage={{param:requestLanguage}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project key or ID
- `formId` (path, string, required) — The ID of the form
- `requestLanguage` (query, string, optional) — The requested language for the form to be translated to

## Original description

Gets a form template as a JSON object on a project.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
