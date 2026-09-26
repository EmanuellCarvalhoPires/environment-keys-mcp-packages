---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-export
  - api/operation/get
  - api/effect/read
up: "[[MCP - Forms]]"
app: "Forms"
method: GET
path: "/export/{exportId}"
category: "Forms Export"
writes_data: false
---
# Forms - Get export status

**Get export status** — `GET /export/{exportId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get export status"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/export/{{param:exportId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `exportId` (path, string, required) — The export task ID

## Original description

Gets the status of an export of form data.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
