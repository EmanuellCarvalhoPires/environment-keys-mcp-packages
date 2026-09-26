---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_issues_in_queue
title: "JSM - Get issues in queue"
kind: request
request: "[[JSM - Get issues in queue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue/{queueId}/issue · Get issues in queue. This method returns the customer requests in a queue. Only fields that the queue is configured to show are returned. For example, if a queue is configured to show description and due date, then only those two fields are returned for each customer request in the queue. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk containing the queue to be queried. This can alternatively be a project identifier."
  "queueId":
    type: string
    required: true
    description: "The ID of the queue whose customer requests will be returned."
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of items to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: false
---
# jsm_get_issues_in_queue

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue/{queueId}/issue` — Get issues in queue

- Request: [[JSM - Get issues in queue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
