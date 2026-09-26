---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/webhooks
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_extend_webhook_life
title: "Jira v3 - Extend webhook life"
kind: request
request: "[[Jira v3 - Extend webhook life]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/webhook/refresh · Extend webhook life. Extends the life of webhook. Webhooks registered through the REST API expire after 30 days. Call this operation to keep them alive. Unrecognized webhook IDs (those that are not found or belong to other apps) are ignored. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_extend_webhook_life

`PUT /rest/api/3/webhook/refresh` — Extend webhook life

- Request: [[Jira v3 - Extend webhook life]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
