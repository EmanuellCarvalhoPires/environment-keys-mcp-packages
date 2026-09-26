---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/webhooks
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_subscribable_webhook_types
title: "Bitbucket - List subscribable webhook types"
kind: request
request: "[[Bitbucket - List subscribable webhook types]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /hook_events/{subject_type} · List subscribable webhook types. Returns a paginated list of all valid webhook events for the specified entity. The team and user webhooks are deprecated, and you should use workspace instead. For more information, see the announcement. This is public data that does not require any scopes or authentication. Writes data: no."
params:
  "subject_type":
    type: string
    required: true
    description: "A resource or subject type."
writes: false
expose: false
---
# bitbucket_list_subscribable_webhook_types

`GET /hook_events/{subject_type}` — List subscribable webhook types

- Request: [[Bitbucket - List subscribable webhook types]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
