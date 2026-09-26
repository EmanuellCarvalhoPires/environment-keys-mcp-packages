---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_property_get
title: "JSM - Get property (GET)"
kind: request
request: "[[JSM - Get property (GET)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey} · Get property. Returns the value of the property from a request type. Properties for a Request Type in next-gen are stored as Issue Type properties and therefore also available by calling the Jira Cloud Platform Get issue type property endpoint. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk which contains the request type. This can alternatively be a project identifier."
  "requestTypeId":
    type: string
    required: true
    description: "The ID of the request type from which the property will be retrieved."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property to return."
writes: false
expose: false
---
# jsm_get_property_get

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}` — Get property

- Request: [[JSM - Get property (GET)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
