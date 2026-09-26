---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_service_desk_by_id
title: "JSM - Get service desk by id"
kind: request
request: "[[JSM - Get service desk by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId} · Get service desk by id. This method returns a service desk. Use this method to get service desk details whenever your application component is passed a service desk ID but needs to display other service desk details. Permissions required: Permission to access the Service Desk. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk to return. This can alternatively be a project identifier."
writes: false
expose: false
---
# jsm_get_service_desk_by_id

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}` — Get service desk by id

- Request: [[JSM - Get service desk by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
