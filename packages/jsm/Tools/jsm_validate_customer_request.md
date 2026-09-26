---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/search
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_validate_customer_request
title: "JSM - Validate customer request"
kind: request
request: "[[JSM - Validate customer request]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/request/validate · Validate customer request. Validates a customer request payload without creating (persisting) a request. This endpoint runs exactly the same structural and semantic validations as Create customer request \\\\u2014 including ProForma form validation \\\\u2014 but performs no mutation: no issue is created and no… Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jsm_validate_customer_request

`POST /rest/servicedeskapi/request/validate` — Validate customer request

- Request: [[JSM - Validate customer request]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
