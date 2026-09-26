---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/webhooks
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_failed_webhooks
title: "Jira v3 - Get failed webhooks"
kind: request
request: "[[Jira v3 - Get failed webhooks]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/webhook/failed · Get failed webhooks. Returns webhooks that have recently failed to be delivered to the requesting app after the maximum number of retries. After 72 hours the failure may no longer be returned by this operation. The oldest failure is returned first. This method uses a cursor-based pagination. Writes data: no."
params:
  "maxResults":
    type: string
    required: false
    description: "The maximum number of webhooks to return per page. If obeying the maxResults directive would result in records with the same failure time being split across pages, the directive is ignored and all rec…"
  "after":
    type: string
    required: false
    description: "The time after which any webhook failure must have occurred for the record to be returned, expressed as milliseconds since the UNIX epoch."
writes: false
expose: false
---
# jira_get_failed_webhooks

`GET /rest/api/3/webhook/failed` — Get failed webhooks

- Request: [[Jira v3 - Get failed webhooks]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
