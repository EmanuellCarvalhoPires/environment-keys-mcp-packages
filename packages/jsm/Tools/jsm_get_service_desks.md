---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_service_desks
title: "JSM - Get service desks"
kind: request
request: "[[JSM - Get service desks]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk · Get service desks. This method returns all the service desks in the Jira Service Management instance that the user has permission to access. Use this method where you need a list of service desks or need to locate a service desk by name or keyword. Writes data: no."
params:
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of items to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: true
---
# jsm_get_service_desks

`GET /rest/servicedeskapi/servicedesk` — Get service desks

- Request: [[JSM - Get service desks]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
