---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/other-operations
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_create_customer_post
title: "JSM - Create customer (POST)"
kind: request
request: "[[JSM - Create customer (POST)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/customer/skip-permission-check · Create customer. Creates a customer account on behalf of jsd-nutmeg. This endpoint is restricted to jsd-nutmeg via ASAP authentication. Writes data: yes."
params:
  "strictConflictStatusCode":
    type: string
    required: false
    description: "Optional boolean flag; when \\{@code true\\}, returns 409 Conflict for duplicate email instead of the default 400."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_create_customer_post

`POST /rest/servicedeskapi/customer/skip-permission-check` — Create customer

- Request: [[JSM - Create customer (POST)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
