---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_webhooks_for_a_workspace
title: "Bitbucket - List webhooks for a workspace"
kind: request
request: "[[Bitbucket - List webhooks for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/hooks · List webhooks for a workspace. Returns a paginated list of webhooks installed on this workspace. Writes data: no."
writes: false
expose: false
---
# bitbucket_list_webhooks_for_a_workspace

`GET /workspaces/{workspace}/hooks` — List webhooks for a workspace

- Request: [[Bitbucket - List webhooks for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
