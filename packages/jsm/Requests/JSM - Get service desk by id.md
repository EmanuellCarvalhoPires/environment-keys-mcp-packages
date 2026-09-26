---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_service_desk_by_id]]"
---
# JSM - Get service desk by id

**Get service desk by id** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}`

- Run by the tool [[jsm_get_service_desk_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk to return. This can alternatively be a project identifier.

## Original description

This method returns a service desk. Use this method to get service desk details whenever your application component is passed a service desk ID but needs to display other service desk details.

**[Permissions](#permissions) required**: Permission to access the Service Desk. For example, being the Service Desk's Administrator or one of its Agents or Users.
