---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_workspace_system_gpg_public_key_s
title: "Bitbucket - Get the workspace system GPG public key(s)"
kind: request
request: "[[Bitbucket - Get the workspace system GPG public key(s)]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/settings/gpg/public-key · Get the workspace system GPG public key(s). Returns the system public GPG key(s). In most cases a single key is returned. During a key rotation period, two keys may be returned. Writes data: no."
writes: false
expose: false
---
# bitbucket_get_the_workspace_system_gpg_public_key_s

`GET /workspaces/{workspace}/settings/gpg/public-key` — Get the workspace system GPG public key(s)

- Request: [[Bitbucket - Get the workspace system GPG public key(s)]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
