---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_retrieve_the_inheritance_state_for_repository_settings
title: "Bitbucket - Retrieve the inheritance state for repository settings"
kind: request
request: "[[Bitbucket - Retrieve the inheritance state for repository settings]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/override-settings · Retrieve the inheritance state for repository settings. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_retrieve_the_inheritance_state_for_repository_settings

`GET /repositories/{workspace}/{repo_slug}/override-settings` — Retrieve the inheritance state for repository settings

- Request: [[Bitbucket - Retrieve the inheritance state for repository settings]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
