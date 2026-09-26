---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_queues
title: "JSM - Get queues"
kind: request
request: "[[JSM - Get queues]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue · Get queues. This method returns the queues in a service desk. To include a customer request count for each queue (in the issueCount field) in the response, set the query parameter includeCount to true (its default is false). Permissions required: service desk's Agent. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "ID of the service desk whose queues will be returned. This can alternatively be a project identifier."
  "includeCount":
    type: string
    required: false
    description: "Specifies whether to include each queue's customer request (issue) count in the response."
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
# jsm_get_queues

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue` — Get queues

- Request: [[JSM - Get queues]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
