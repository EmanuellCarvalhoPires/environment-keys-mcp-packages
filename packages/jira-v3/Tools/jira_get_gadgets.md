---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_gadgets
title: "Jira v3 - Get gadgets"
kind: request
request: "[[Jira v3 - Get gadgets]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/dashboard/{dashboardId}/gadget · Get gadgets. Returns a list of dashboard gadgets on a dashboard. This operation returns: Gadgets from a list of IDs, when id is set. Gadgets with a module key, when moduleKey is set. Gadgets from a list of URIs, when uri is set. All gadgets, when no other parameters are set. Writes data: no."
params:
  "dashboardId":
    type: string
    required: true
    description: "The ID of the dashboard."
  "moduleKey":
    type: string
    required: false
    description: "The list of gadgets module keys. To include multiple module keys, separate module keys with ampersand: moduleKey=key:one&moduleKey=key:two."
  "uri":
    type: string
    required: false
    description: "The list of gadgets URIs. To include multiple URIs, separate URIs with ampersand: uri=/rest/example/uri/1&uri=/rest/example/uri/2."
  "gadgetId":
    type: string
    required: false
    description: "The list of gadgets IDs. To include multiple IDs, separate IDs with ampersand: gadgetId=10000&gadgetId=10001."
writes: false
expose: false
---
# jira_get_gadgets

`GET /rest/api/3/dashboard/{dashboardId}/gadget` — Get gadgets

- Request: [[Jira v3 - Get gadgets]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
