---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_attachments_for_request
title: "JSM - Get attachments for request"
kind: request
request: "[[JSM - Get attachments for request]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment · Get attachments for request. This method returns all the attachments for a customer requests. Permissions required: Permission to view the customer request. Response limitations: Customers will only get a list of public attachments. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request from which the attachments will be listed."
  "start":
    type: string
    required: true
    description: "The starting index of the returned attachment. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: true
    description: "The maximum number of comments to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: false
---
# jsm_get_attachments_for_request

`GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment` — Get attachments for request

- Request: [[JSM - Get attachments for request]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
