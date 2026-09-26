---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_create_customer_request
title: "JSM - Create customer request"
kind: request
request: "[[JSM - Create customer request]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/request · Create customer request. This method creates a customer request in a service desk. The JSON request must include the service desk and customer request type, as well as any fields that are required for the request type. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: true
---
# jsm_create_customer_request

`POST /rest/servicedeskapi/request` — Create customer request

- Request: [[JSM - Create customer request]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
