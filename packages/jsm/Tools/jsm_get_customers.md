---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_customers
title: "JSM - Get customers"
kind: request
request: "[[JSM - Get customers]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer · Get customers. This method returns a list of the customers on a service desk. The returned list of customers can be filtered using the query parameter. The parameter is matched against customers' displayName, name, or email. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk the customer list should be returned from. This can alternatively be a project identifier."
  "query":
    type: string
    required: false
    description: "The string used to filter the customer list."
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of users to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: false
---
# jsm_get_customers

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer` — Get customers

- Request: [[JSM - Get customers]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
