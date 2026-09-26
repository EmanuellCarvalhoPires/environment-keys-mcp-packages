---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_properties_keys_get
title: "JSM - Get properties keys (GET)"
kind: request
request: "[[JSM - Get properties keys (GET)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property · Get properties keys. Returns the keys of all properties for a request type. Properties for a Request Type in next-gen are stored as Issue Type properties and therefore the keys of all properties for a request type are also available by calling the Jira Cloud Platform Get issue type property keys endp… Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk which contains the request type. This can alternatively be a project identifier."
  "requestTypeId":
    type: string
    required: true
    description: "The ID of the request type for which keys will be retrieved."
writes: false
expose: false
---
# jsm_get_properties_keys_get

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property` — Get properties keys

- Request: [[JSM - Get properties keys (GET)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
