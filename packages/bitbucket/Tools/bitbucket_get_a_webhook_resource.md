---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/webhooks
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_webhook_resource
title: "Bitbucket - Get a webhook resource"
kind: request
request: "[[Bitbucket - Get a webhook resource]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /hook_events · Get a webhook resource. Returns the webhook resource or subject types on which webhooks can be registered. Each resource/subject type contains an events link that returns the paginated list of specific events each individual subject type can emit. Writes data: no."
writes: false
expose: false
---
# bitbucket_get_a_webhook_resource

`GET /hook_events` — Get a webhook resource

- Request: [[Bitbucket - Get a webhook resource]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
