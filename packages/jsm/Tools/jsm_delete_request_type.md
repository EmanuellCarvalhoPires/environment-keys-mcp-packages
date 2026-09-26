---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_delete_request_type
title: "JSM - Delete request type"
kind: request
request: "[[JSM - Delete request type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId} · Delete request type. This method deletes a customer request type from a service desk, and removes it from all customer requests. This only supports classic projects. Permissions required: Service desk administrator. Writes data: yes."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID or project identifier of the service desk."
  "requestTypeId":
    type: string
    required: true
    description: "The ID of the request type."
writes: true
expose: false
---
# jsm_delete_request_type

`DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}` — Delete request type

- Request: [[JSM - Delete request type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
