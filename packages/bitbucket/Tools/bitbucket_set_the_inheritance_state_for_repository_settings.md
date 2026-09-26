---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_set_the_inheritance_state_for_repository_settings
title: "Bitbucket - Set the inheritance state for repository settings"
kind: request
request: "[[Bitbucket - Set the inheritance state for repository settings]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/override-settings · Set the inheritance state for repository settings. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: true
expose: false
---
# bitbucket_set_the_inheritance_state_for_repository_settings

`PUT /repositories/{workspace}/{repo_slug}/override-settings` — Set the inheritance state for repository settings

- Request: [[Bitbucket - Set the inheritance state for repository settings]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
