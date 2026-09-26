---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_pull_requests
title: "Bitbucket - List pull requests"
kind: request
request: "[[Bitbucket - List pull requests]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pullrequests · List pull requests. Returns all pull requests on the specified repository. By default only open pull requests are returned. This can be controlled using the state query parameter. To retrieve pull requests that are in one of multiple states, repeat the state parameter for each individual state. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "state":
    type: string
    required: false
    description: "Only return pull requests that are in this state. This parameter can be repeated."
writes: false
expose: true
---
# bitbucket_list_pull_requests

`GET /repositories/{workspace}/{repo_slug}/pullrequests` — List pull requests

- Request: [[Bitbucket - List pull requests]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
