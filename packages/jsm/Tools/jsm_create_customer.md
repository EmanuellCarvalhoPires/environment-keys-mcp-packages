---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/customer
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_create_customer
title: "JSM - Create customer"
kind: request
request: "[[JSM - Create customer]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/customer · Create customer. This method adds a customer to the Jira Service Management instance by passing a JSON file including an email address and display name. The display name does not need to be unique. The record's identifiers, name and key, are automatically generated from the request details. Writes data: yes."
params:
  "strictConflictStatusCode":
    type: string
    required: false
    description: "Optional boolean flag to return 409 Conflict status code for duplicate customer creation request"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_create_customer

`POST /rest/servicedeskapi/customer` — Create customer

- Request: [[JSM - Create customer]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
