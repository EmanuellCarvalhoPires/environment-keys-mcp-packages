---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-export
  - api/operation/action
  - api/effect/write
up: "[[MCP - Forms]]"
app: "Forms"
method: POST
path: "/export"
category: "Forms Export"
writes_data: true
---
# Forms - Start export

**Start export** — `POST /export`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Start export"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
POST https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/export
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Starts an export of form data on a project.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
