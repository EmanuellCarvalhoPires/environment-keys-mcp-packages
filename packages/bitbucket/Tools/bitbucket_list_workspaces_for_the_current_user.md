---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_workspaces_for_the_current_user
title: "Bitbucket - List workspaces for the current user"
kind: request
request: "[[Bitbucket - List workspaces for the current user]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /user/workspaces · List workspaces for the current user. Returns an object for each workspace accessible to the caller. This object also contains details on whether the caller has admin permissions on the workspace (\"administrator\" = true) or not (\"administrator\" = false). Writes data: no."
params:
  "sort":
    type: string
    required: false
    description: "Name of a response property to sort results (only slug is supported)."
  "administrator":
    type: string
    required: false
    description: "Filter workspaces based on which ones the caller has admin permissions or not."
writes: false
expose: false
---
# bitbucket_list_workspaces_for_the_current_user

`GET /user/workspaces` — List workspaces for the current user

- Request: [[Bitbucket - List workspaces for the current user]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
