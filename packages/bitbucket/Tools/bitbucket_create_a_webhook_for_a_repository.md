---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_webhook_for_a_repository
title: "Bitbucket - Create a webhook for a repository"
kind: request
request: "[[Bitbucket - Create a webhook for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/hooks · Create a webhook for a repository. Creates a new webhook on the specified repository. Example: $ curl -X POST -u credentials -H 'Content-Type: application/json' https://api.bitbucket.org/2.0/repositories/my-workspace/my-repo-slug/hooks -d ' { \"description\": \"Webhook Description\", \"url\": \"https://example.com/\", \"ac… Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: true
expose: false
---
# bitbucket_create_a_webhook_for_a_repository

`POST /repositories/{workspace}/{repo_slug}/hooks` — Create a webhook for a repository

- Request: [[Bitbucket - Create a webhook for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
