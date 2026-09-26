---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/users
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_user
title: "Bitbucket - Get a user"
kind: request
request: "[[Bitbucket - Get a user]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /users/{selected_user} · Get a user. Gets the public information associated with a user account. If the user's profile is private, location, website and createdon elements are omitted. Note that the user object returned by this operation is changing significantly, due to privacy changes. Writes data: no."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
writes: false
expose: false
---
# bitbucket_get_a_user

`GET /users/{selected_user}` — Get a user

- Request: [[Bitbucket - Get a user]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
