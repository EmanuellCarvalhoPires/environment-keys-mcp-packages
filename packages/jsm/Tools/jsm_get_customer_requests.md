---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_customer_requests
title: "JSM - Get customer requests"
kind: request
request: "[[JSM - Get customer requests]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request · Get customer requests. This method returns all customer requests for the user executing the query. The returned customer requests are ordered chronologically by the latest activity on each request. For example, the latest status transition or comment. Writes data: no."
params:
  "searchTerm":
    type: string
    required: false
    description: "Filters customer requests where the request summary matches the searchTerm. Wildcards can be used in the searchTerm parameter."
  "requestOwnership":
    type: string
    required: false
    description: "Filters customer requests using the following values: OWNEDREQUESTS returns customer requests where the user is the creator."
  "requestStatus":
    type: string
    required: false
    description: "Filters customer requests where the request is closed, open, or either of the two where: CLOSEDREQUESTS returns customer requests that are closed."
  "approvalStatus":
    type: string
    required: false
    description: "Filters results to customer requests based on their approval status: MYPENDINGAPPROVAL returns customer requests pending the user's approval."
  "organizationId":
    type: string
    required: false
    description: "Filters customer requests that belong to a specific organization (note that the user must be a member of that organization). Note: Valid only when used with requestOwnership=ORGANIZATION."
  "serviceDeskId":
    type: string
    required: false
    description: "Filters customer requests by service desk."
  "requestTypeId":
    type: string
    required: false
    description: "Filters customer requests by request type. Note that the serviceDeskId must be specified for the service desk in which the request type belongs."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the customer request to expand, where: serviceDesk returns additional details for each service desk."
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of items to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: true
---
# jsm_get_customer_requests

`GET /rest/servicedeskapi/request` — Get customer requests

- Request: [[JSM - Get customer requests]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
