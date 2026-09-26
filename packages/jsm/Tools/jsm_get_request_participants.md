---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_request_participants
title: "JSM - Get request participants"
kind: request
request: "[[JSM - Get request participants]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/participant · Get request participants. This method returns a list of all the participants on a customer request. Permissions required: Permission to view the customer request. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to be queried for its participants."
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of request types to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: false
---
# jsm_get_request_participants

`GET /rest/servicedeskapi/request/{issueIdOrKey}/participant` — Get request participants

- Request: [[JSM - Get request participants]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
