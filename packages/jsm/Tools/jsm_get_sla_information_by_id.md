---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_sla_information_by_id
title: "JSM - Get sla information by id"
kind: request
request: "[[JSM - Get sla information by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/sla/{slaMetricId} · Get sla information by id. This method returns the details for an SLA on a customer request. Permissions required: Agent for the Service Desk containing the queried customer request, AND Browse Projects permission on the project containing the customer request, including any restrictions imposed by issue s… Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request whose SLAs will be retrieved."
  "slaMetricId":
    type: string
    required: true
    description: "The ID or key of the SLAs metric to be retrieved."
writes: false
expose: false
---
# jsm_get_sla_information_by_id

`GET /rest/servicedeskapi/request/{issueIdOrKey}/sla/{slaMetricId}` — Get sla information by id

- Request: [[JSM - Get sla information by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
