---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_request_type_groups
title: "JSM - Get request type groups"
kind: request
request: "[[JSM - Get request type groups]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttypegroup · Get request type groups. This method returns a service desk's customer request type groups. Jira Service Management administrators can arrange the customer request type groups in an arbitrary order for display on the customer portal; the groups are returned in this order. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk whose customer request type groups are to be returned. This can alternatively be a project identifier."
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of items to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: false
---
# jsm_get_request_type_groups

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttypegroup` — Get request type groups

- Request: [[JSM - Get request type groups]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
