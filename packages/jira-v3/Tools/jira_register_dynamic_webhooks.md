---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/webhooks
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_register_dynamic_webhooks
title: "Jira v3 - Register dynamic webhooks"
kind: request
request: "[[Jira v3 - Register dynamic webhooks]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/webhook · Register dynamic webhooks. Registers webhooks. NOTE: for non-public OAuth apps, webhooks are delivered only if there is a match between the app owner and the user who registered a dynamic webhook. Permissions required: Only Connect and OAuth 2.0 apps can use this operation. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_register_dynamic_webhooks

`POST /rest/api/3/webhook` — Register dynamic webhooks

- Request: [[Jira v3 - Register dynamic webhooks]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
