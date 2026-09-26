---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-project
  - api/operation/create
  - api/effect/write
up: "[[MCP - Forms]]"
app: "Forms"
method: POST
path: "/project/{projectIdOrKey}/form"
category: "Forms on Project"
writes_data: true
---
# Forms - Create form template

**Create form template** — `POST /project/{projectIdOrKey}/form`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Create form template"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
POST https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/project/{{param:projectIdOrKey}}/form
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project key or ID
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a form template on a project.

**[Permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#permissions) required:**

 *  *Administer Jira* [project permission](https://confluence.atlassian.com/x/yodKLg).
