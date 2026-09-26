---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/requesttype
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_all_request_types
title: "JSM - Get all request types"
kind: request
request: "[[JSM - Get all request types]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/requesttype · Get all request types. This method returns all customer request types used in the Jira Service Management instance, optionally filtered by a query string. Use servicedeskapi/servicedesk/\\{serviceDeskId\\}/requesttype to find the customer request types supported by a specific service desk. Writes data: no."
params:
  "searchQuery":
    type: string
    required: false
    description: "String to be used to filter the results."
  "serviceDeskId":
    type: string
    required: false
    description: "Filter the request types by service desk Ids provided. Multiple values of the query parameter are supported."
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of items to return per page. Default: 50. See the Pagination section for more details."
  "expand":
    type: string
    required: false
    description: "Query parameter expand."
  "includeHiddenRequestTypesInSearch":
    type: string
    required: false
    description: "Whether to include hidden request types when searching with searchQuery."
  "restrictionStatus":
    type: string
    required: false
    description: "Request type restriction status (open or restricted) used to filter the results."
writes: false
expose: false
---
# jsm_get_all_request_types

`GET /rest/servicedeskapi/requesttype` — Get all request types

- Request: [[JSM - Get all request types]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
