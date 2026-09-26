---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_webhook_for_a_workspace
title: "Bitbucket - Update a webhook for a workspace"
kind: request
request: "[[Bitbucket - Update a webhook for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /workspaces/{workspace}/hooks/{uid} · Update a webhook for a workspace. Updates the specified webhook subscription. The following properties can be mutated: description url secret active events The hook's secret is used as a key to generate the HMAC hex digest sent in the X-Hub-Signature header at delivery time. Writes data: yes."
params:
  "uid":
    type: string
    required: true
    description: "Value of uid in the path."
writes: true
expose: false
---
# bitbucket_update_a_webhook_for_a_workspace

`PUT /workspaces/{workspace}/hooks/{uid}` — Update a webhook for a workspace

- Request: [[Bitbucket - Update a webhook for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
