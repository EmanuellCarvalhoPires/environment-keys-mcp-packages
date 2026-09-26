---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_customer_transitions
title: "JSM - Get customer transitions"
kind: request
request: "[[JSM - Get customer transitions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/transition · Get customer transitions. This method returns a list of transitions, the workflow processes that moves a customer request from one status to another, that the user can perform on a request. Use this method to provide a user with a list if the actions they can take on a customer request. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request whose transitions will be retrieved."
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
# jsm_get_customer_transitions

`GET /rest/servicedeskapi/request/{issueIdOrKey}/transition` — Get customer transitions

- Request: [[JSM - Get customer transitions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
