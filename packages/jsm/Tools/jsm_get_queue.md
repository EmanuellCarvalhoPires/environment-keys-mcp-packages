---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_queue
title: "JSM - Get queue"
kind: request
request: "[[JSM - Get queue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue/{queueId} · Get queue. This method returns a specific queues in a service desk. To include a customer request count for the queue (in the issueCount field) in the response, set the query parameter includeCount to true (its default is false). Permissions required: service desk's Agent. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "ID of the service desk whose queues will be returned. This can alternatively be a project identifier."
  "queueId":
    type: string
    required: true
    description: "ID of the required queue."
  "includeCount":
    type: string
    required: false
    description: "Specifies whether to include each queue's customer request (issue) count in the response."
writes: false
expose: false
---
# jsm_get_queue

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue/{queueId}` — Get queue

- Request: [[JSM - Get queue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
