---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_request_type_by_id
title: "JSM - Get request type by id"
kind: request
request: "[[JSM - Get request type by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId} · Get request type by id. This method returns a customer request type from a service desk. This operation can be accessed anonymously. Permissions required: Permission to access the service desk. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk whose customer request type is to be returned. This can alternatively be a project identifier."
  "requestTypeId":
    type: string
    required: true
    description: "The ID of the customer request type to be returned."
  "expand":
    type: string
    required: false
    description: "Query parameter expand."
writes: false
expose: false
---
# jsm_get_request_type_by_id

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}` — Get request type by id

- Request: [[JSM - Get request type by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
