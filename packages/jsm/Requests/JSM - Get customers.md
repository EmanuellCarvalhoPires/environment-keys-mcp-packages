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
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/customer"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_customers]]"
---
# JSM - Get customers

**Get customers** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer`

- Run by the tool [[jsm_get_customers]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/customer?query={{param:query}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk the customer list should be returned from. This can alternatively be a project identifier.
- `query` (query, string, optional) — The string used to filter the customer list.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of users to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns a list of the customers on a service desk.

The returned list of customers can be filtered using the `query` parameter. The parameter is matched against customers' `displayName`, `name`, or `email`. For example, searching for "John", "Jo", "Smi", or "Smith" will match a user with display name "John Smith".

**[Permissions](#permissions) required**: Permission to view this Service Desk's customers.
