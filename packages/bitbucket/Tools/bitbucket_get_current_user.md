---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_current_user
title: "Bitbucket - Get current user"
kind: request
request: "[[Bitbucket - Get current user]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /user · Get current user. Returns the currently logged in user. Writes data: no."
writes: false
expose: true
---
# bitbucket_get_current_user

`GET /user` — Get current user

- Request: [[Bitbucket - Get current user]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
