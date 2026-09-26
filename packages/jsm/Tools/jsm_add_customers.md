---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_add_customers
title: "JSM - Add customers"
kind: request
request: "[[JSM - Add customers]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer · Add customers. Adds one or more customers to a service desk. If any of the passed customers are associated with the service desk, no changes will be made for those customers and the resource returns a 204 success code. Permissions required: Service desk administrator Writes data: yes."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk the customer list should be returned from. This can alternatively be a project identifier."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_add_customers

`POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer` — Add customers

- Request: [[JSM - Add customers]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
