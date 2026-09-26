---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/webhooks
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_dynamic_webhooks_for_app
title: "Jira v3 - Get dynamic webhooks for app"
kind: request
request: "[[Jira v3 - Get dynamic webhooks for app]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/webhook · Get dynamic webhooks for app. Returns a paginated list of the webhooks registered by the calling app. Permissions required: Only Connect and OAuth 2.0 apps can use this operation. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
writes: false
expose: false
---
# jira_get_dynamic_webhooks_for_app

`GET /rest/api/3/webhook` — Get dynamic webhooks for app

- Request: [[Jira v3 - Get dynamic webhooks for app]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
