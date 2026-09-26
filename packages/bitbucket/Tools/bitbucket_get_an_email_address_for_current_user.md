---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/users
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_an_email_address_for_current_user
title: "Bitbucket - Get an email address for current user"
kind: request
request: "[[Bitbucket - Get an email address for current user]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /user/emails/{email} · Get an email address for current user. Returns details about a specific one of the authenticated user's email addresses. Details describe whether the address has been confirmed by the user and whether it is the user's primary address or not. Writes data: no."
params:
  "email":
    type: string
    required: true
    description: "Value of email in the path."
writes: false
expose: false
---
# bitbucket_get_an_email_address_for_current_user

`GET /user/emails/{email}` — Get an email address for current user

- Request: [[Bitbucket - Get an email address for current user]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
