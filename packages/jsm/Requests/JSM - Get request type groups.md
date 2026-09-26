---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttypegroup"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_request_type_groups]]"
---
# JSM - Get request type groups

**Get request type groups** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttypegroup`

- Run by the tool [[jsm_get_request_type_groups]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttypegroup?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk whose customer request type groups are to be returned. This can alternatively be a project identifier.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of items to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns a service desk's customer request type groups. Jira Service Management administrators can arrange the customer request type groups in an arbitrary order for display on the customer portal; the groups are returned in this order.

**[Permissions](#permissions) required**: Permission to view the service desk.
