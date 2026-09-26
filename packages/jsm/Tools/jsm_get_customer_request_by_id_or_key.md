---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_customer_request_by_id_or_key
title: "JSM - Get customer request by id or key"
kind: request
request: "[[JSM - Get customer request by id or key]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey} · Get customer request by id or key. This method returns a customer request. Permissions required: Permission to access the specified service desk. Response limitations: For customers, only a request they created, was created on their behalf, or they are participating in will be returned. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or Key of the customer request to be returned"
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the customer request to expand, where: serviceDesk returns additional service desk details."
writes: false
expose: false
---
# jsm_get_customer_request_by_id_or_key

`GET /rest/servicedeskapi/request/{issueIdOrKey}` — Get customer request by id or key

- Request: [[JSM - Get customer request by id or key]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
