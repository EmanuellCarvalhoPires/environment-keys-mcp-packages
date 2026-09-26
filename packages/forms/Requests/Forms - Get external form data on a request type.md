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
path: "/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/form/externaldata"
category: "Forms on Portal"
writes_data: false
---
# Forms - Get external form data on a request type

**Get external form data on a request type** — `GET /servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/form/externaldata`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Forms - Get external form data on a request type"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
GET https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/servicedesk/{{param:serviceDeskId}}/requesttype/{{param:requestTypeId}}/form/externaldata
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The service desk ID. This can alternatively be a project identifier.
- `requestTypeId` (path, string, required) — The request type ID

## Original description

Get all external form data for questions and default answers on a form added to a request type. Forms can be linked to external sources including Jira fields and data connections, with this API returning the latest responses on these linked fields.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *View Service Desk* permission to view the service desk.

**Disclaimer:** This endpoint may return choice labels sourced from externally-configured data sources outside Atlassian's control. Treat these values as untrusted plain text and apply appropriate output encoding before rendering in any HTML context. See [Data connection choice labels](/cloud/forms/rest/#data-connection-choice-labels).
