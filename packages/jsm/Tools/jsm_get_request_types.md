---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_request_types
title: "JSM - Get request types"
kind: request
request: "[[JSM - Get request types]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype · Get request types. This method returns all customer request types from a service desk. There are two parameters for filtering the returned list: groupId which filters the results to items in the customer request type group. searchQuery which is matched against request types' name or description. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk whose customer request types are to be returned. This can alternatively be a project identifier."
  "groupId":
    type: string
    required: false
    description: "Filters results to those in a customer request type group."
  "expand":
    type: string
    required: false
    description: "Query parameter expand."
  "searchQuery":
    type: string
    required: false
    description: "The string to be used to filter the results."
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of items to return per page. Default: 50. See the Pagination section for more details."
  "includeHiddenRequestTypesInSearch":
    type: string
    required: false
    description: "Whether to include hidden request types when searching with searchQuery."
  "restrictionStatus":
    type: string
    required: false
    description: "Request type restriction status (open or restricted) used to filter the results."
writes: false
expose: true
---
# jsm_get_request_types

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype` — Get request types

- Request: [[JSM - Get request types]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
