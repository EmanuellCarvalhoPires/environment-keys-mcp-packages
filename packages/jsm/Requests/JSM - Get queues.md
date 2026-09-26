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
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/queue"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_queues]]"
---
# JSM - Get queues

**Get queues** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue`

- Run by the tool [[jsm_get_queues]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/queue?includeCount={{param:includeCount}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — ID of the service desk whose queues will be returned. This can alternatively be a project identifier.
- `includeCount` (query, string, optional) — Specifies whether to include each queue's customer request (issue) count in the response.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of items to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns the queues in a service desk. To include a customer request count for each queue (in the `issueCount` field) in the response, set the query parameter `includeCount` to true (its default is false).

**[Permissions](#permissions) required**: service desk's Agent.
