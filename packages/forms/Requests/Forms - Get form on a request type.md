---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-portal
  - api/operation/list
  - api/effect/read
up: "[[MCP - Forms]]"
app: "Forms"
method: GET
path: "/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/form"
category: "Forms on Portal"
writes_data: false
---
# Forms - Get form on a request type

**Get form on a request type** — `GET /servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/form`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get form on a request type"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/servicedesk/{{param:serviceDeskId}}/requesttype/{{param:requestTypeId}}/form?requestLanguage={{param:requestLanguage}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The service desk ID. This can alternatively be a project identifier.
- `requestTypeId` (path, string, required) — The request type ID
- `requestLanguage` (query, string, optional) — The requested language for the form to be translated to

## Original description

Gets a form template as a JSON object on a request type.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *View Service Desk* permission to view the service desk.
