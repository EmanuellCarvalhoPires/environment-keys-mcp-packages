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
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/queue/{queueId}/issue"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_issues_in_queue]]"
---
# JSM - Get issues in queue

**Get issues in queue** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue/{queueId}/issue`

- Run by the tool [[jsm_get_issues_in_queue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/queue/{{param:queueId}}/issue?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk containing the queue to be queried. This can alternatively be a project identifier.
- `queueId` (path, string, required) — The ID of the queue whose customer requests will be returned.
- `start` (query, string, optional) — The starting index of the returned objects. Base index: 0. See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of items to return per page. Default: 50. See the Pagination section for more details.

## Original description

This method returns the customer requests in a queue. Only fields that the queue is configured to show are returned. For example, if a queue is configured to show description and due date, then only those two fields are returned for each customer request in the queue.

**[Permissions](#permissions) required**: Service desk's agent.
