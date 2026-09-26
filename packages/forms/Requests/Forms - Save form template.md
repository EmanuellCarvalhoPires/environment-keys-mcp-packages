---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-project
  - api/operation/update
  - api/effect/write
up: "[[MCP - Forms]]"
app: "Forms"
method: PUT
path: "/project/{projectIdOrKey}/form/{formId}"
category: "Forms on Project"
writes_data: true
---
# Forms - Save form template

**Save form template** — `PUT /project/{projectIdOrKey}/form/{formId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Save form template"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
PUT https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/project/{{param:projectIdOrKey}}/form/{{param:formId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project key or ID
- `formId` (path, string, required) — The ID of the form
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Saves a form template on a project.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Administer Jira* [project permission](https://confluence.atlassian.com/x/yodKLg).
