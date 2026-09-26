---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_email_addresses_for_current_user
title: "Bitbucket - List email addresses for current user"
kind: request
request: "[[Bitbucket - List email addresses for current user]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /user/emails · List email addresses for current user. Returns all the authenticated user's email addresses. Both confirmed and unconfirmed. Writes data: no."
writes: false
expose: false
---
# bitbucket_list_email_addresses_for_current_user

`GET /user/emails` — List email addresses for current user

- Request: [[Bitbucket - List email addresses for current user]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
