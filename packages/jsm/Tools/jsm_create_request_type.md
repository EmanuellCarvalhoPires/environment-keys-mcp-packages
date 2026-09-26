---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_create_request_type
title: "JSM - Create request type"
kind: request
request: "[[JSM - Create request type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype · Create request type. This method enables a customer request type to be added to a service desk based on an issue type. Note that not all customer request type fields can be specified in the request and these fields are given the following default values: Request type icon is given the headset icon. Writes data: yes."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk where the customer request type is to be created. This can alternatively be a project identifier."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_create_request_type

`POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype` — Create request type

- Request: [[JSM - Create request type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
