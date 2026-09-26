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
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/queue/{queueId}"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_queue]]"
---
# JSM - Get queue

**Get queue** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue/{queueId}`

- Run by the tool [[jsm_get_queue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/queue/{{param:queueId}}?includeCount={{param:includeCount}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — ID of the service desk whose queues will be returned. This can alternatively be a project identifier.
- `queueId` (path, string, required) — ID of the required queue.
- `includeCount` (query, string, optional) — Specifies whether to include each queue's customer request (issue) count in the response.

## Original description

This method returns a specific queues in a service desk. To include a customer request count for the queue (in the `issueCount` field) in the response, set the query parameter `includeCount` to true (its default is false).

**[Permissions](#permissions) required**: service desk's Agent.
