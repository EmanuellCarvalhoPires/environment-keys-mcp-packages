---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/other-operations
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_add_customers_post
title: "JSM - Add customers (POST)"
kind: request
request: "[[JSM - Add customers (POST)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer/skip-permission-check · Add customers. Adds one or more customers to a service desk on behalf of jsd-nutmeg. This endpoint is restricted to jsd-nutmeg via ASAP authentication. Writes data: yes."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk to add customers to. This can alternatively be a project identifier."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_add_customers_post

`POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer/skip-permission-check` — Add customers

- Request: [[JSM - Add customers (POST)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
