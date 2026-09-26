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
path: "/rest/servicedeskapi/servicedesk"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_service_desks]]"
---
# JSM - Get service desks

**Get service desks** — `GET /rest/servicedeskapi/servicedesk`

- Run by the tool [[jsm_get_service_desks]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of items to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns all the service desks in the Jira Service Management instance that the user has permission to access. Use this method where you need a list of service desks or need to locate a service desk by name or keyword.

**Note:** This method will be slow if the instance has hundreds of service desks. If you want to fetch a single service desk by its ID, use [/rest/servicedeskapi/servicedesk/\{serviceDeskId\}](./#api-rest-servicedeskapi-servicedesk-servicedeskid-get) instead.

**[Permissions](#permissions) required**: Any
