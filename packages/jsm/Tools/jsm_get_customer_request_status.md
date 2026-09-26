---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_customer_request_status
title: "JSM - Get customer request status"
kind: request
request: "[[JSM - Get customer request status]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/status · Get customer request status. This method returns a list of all the statuses a customer Request has achieved. A status represents the state of an issue in its workflow. An issue can have one active status only. The list returns the status history in chronological order, most recent (current) status first. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to be retrieved."
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
# jsm_get_customer_request_status

`GET /rest/servicedeskapi/request/{issueIdOrKey}/status` — Get customer request status

- Request: [[JSM - Get customer request status]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
