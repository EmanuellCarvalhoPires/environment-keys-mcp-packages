---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_webhook_for_a_repository
title: "Bitbucket - Get a webhook for a repository"
kind: request
request: "[[Bitbucket - Get a webhook for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/hooks/{uid} · Get a webhook for a repository. Returns the webhook with the specified id installed on the specified repository. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "uid":
    type: string
    required: true
    description: "Value of uid in the path."
writes: false
expose: false
---
# bitbucket_get_a_webhook_for_a_repository

`GET /repositories/{workspace}/{repo_slug}/hooks/{uid}` — Get a webhook for a repository

- Request: [[Bitbucket - Get a webhook for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
