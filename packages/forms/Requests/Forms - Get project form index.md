---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-project
  - api/operation/list
  - api/effect/read
up: "[[MCP - Forms]]"
app: "Forms"
method: GET
path: "/project/{projectIdOrKey}/form"
category: "Forms on Project"
writes_data: false
---
# Forms - Get project form index

**Get project form index** — `GET /project/{projectIdOrKey}/form`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get project form index"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/project/{{param:projectIdOrKey}}/form
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project key or ID

## Original description

Get a list of form templates associated with the project.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
