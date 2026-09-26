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
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_request_type_by_id]]"
---
# JSM - Get request type by id

**Get request type by id** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}`

- Run by the tool [[jsm_get_request_type_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttype/{{param:requestTypeId}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk whose customer request type is to be returned. This can alternatively be a project identifier.
- `requestTypeId` (path, string, required) — The ID of the customer request type to be returned.
- `expand` (query, string, optional) — Query parameter expand.

## Original description

This method returns a customer request type from a service desk.

This operation can be accessed anonymously.

**[Permissions](#permissions) required**: Permission to access the service desk.
