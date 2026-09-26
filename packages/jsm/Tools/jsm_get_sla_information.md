---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_sla_information
title: "JSM - Get sla information"
kind: request
request: "[[JSM - Get sla information]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/sla · Get sla information. This method returns all the SLA records on a customer request. A customer request can have zero or more SLAs. Each SLA can have recordings for zero or more \"completed cycles\" and zero or 1 \"ongoing cycle\". Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request whose SLAs will be retrieved."
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
# jsm_get_sla_information

`GET /rest/servicedeskapi/request/{issueIdOrKey}/sla` — Get sla information

- Request: [[JSM - Get sla information]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
