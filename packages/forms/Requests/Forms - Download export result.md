---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-export
  - api/operation/get
  - api/effect/read
  - api/format/binary
up: "[[MCP - Forms]]"
app: "Forms"
method: GET
path: "/export/{exportId}/{filename}"
category: "Forms Export"
writes_data: false
---
# Forms - Download export result

**Download export result** — `GET /export/{exportId}/{filename}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Download export result"`.
- **Format:** the response is binary (file/image); the plugin returns the body as text.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/export/{{param:exportId}}/{{param:filename}}
Authorization: {{service.auth_token}}
Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
```

## Parameters

- `exportId` (path, string, required) — The export task ID
- `filename` (path, string, required) — The name of the file to export to

## Original description

Downloads the result of an export of form data.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
