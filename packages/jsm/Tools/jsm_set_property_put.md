---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_set_property_put
title: "JSM - Set property (PUT)"
kind: request
request: "[[JSM - Set property (PUT)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · PUT /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey} · Set property. Sets the value of a request type property. Use this resource to store custom data against a request type. Writes data: yes."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk which contains the request type. This can alternatively be a project identifier."
  "requestTypeId":
    type: string
    required: true
    description: "The ID of the request type on which the property will be set."
  "propertyKey":
    type: string
    required: true
    description: "The key of the request type property. The maximum length of the key is 255 bytes."
writes: true
expose: false
---
# jsm_set_property_put

`PUT /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}` — Set property

- Request: [[JSM - Set property (PUT)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
