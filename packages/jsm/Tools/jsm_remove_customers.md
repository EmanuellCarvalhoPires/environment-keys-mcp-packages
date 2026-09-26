---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_remove_customers
title: "JSM - Remove customers"
kind: request
request: "[[JSM - Remove customers]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer · Remove customers. This method removes one or more customers from a service desk. The service desk must have closed access. If any of the passed customers are not associated with the service desk, no changes will be made for those customers and the resource returns a 204 success code. Writes data: yes."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk the customers should be removed from. This can alternatively be a project identifier."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_remove_customers

`DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer` — Remove customers

- Request: [[JSM - Remove customers]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
