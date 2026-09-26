---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_approvals
title: "JSM - Get approvals"
kind: request
request: "[[JSM - Get approvals]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/approval · Get approvals. This method returns all approvals on a customer request. Permissions required: Permission to view the customer request. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to be queried for its approvals."
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of approvals to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: false
---
# jsm_get_approvals

`GET /rest/servicedeskapi/request/{issueIdOrKey}/approval` — Get approvals

- Request: [[JSM - Get approvals]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
