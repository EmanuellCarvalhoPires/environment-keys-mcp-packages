---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_webhook_for_a_workspace
title: "Bitbucket - Create a webhook for a workspace"
kind: request
request: "[[Bitbucket - Create a webhook for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /workspaces/{workspace}/hooks · Create a webhook for a workspace. Creates a new webhook on the specified workspace. Workspace webhooks are fired for events from all repositories contained by that workspace. Writes data: yes."
writes: true
expose: false
---
# bitbucket_create_a_webhook_for_a_workspace

`POST /workspaces/{workspace}/hooks` — Create a webhook for a workspace

- Request: [[Bitbucket - Create a webhook for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
