---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_webhook_for_a_workspace
title: "Bitbucket - Get a webhook for a workspace"
kind: request
request: "[[Bitbucket - Get a webhook for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/hooks/{uid} · Get a webhook for a workspace. Returns the webhook with the specified id installed on the given workspace. Writes data: no."
params:
  "uid":
    type: string
    required: true
    description: "Value of uid in the path."
writes: false
expose: false
---
# bitbucket_get_a_webhook_for_a_workspace

`GET /workspaces/{workspace}/hooks/{uid}` — Get a webhook for a workspace

- Request: [[Bitbucket - Get a webhook for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
