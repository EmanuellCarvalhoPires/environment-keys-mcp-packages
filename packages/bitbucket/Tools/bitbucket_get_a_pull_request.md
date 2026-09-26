---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_pull_request
title: "Bitbucket - Get a pull request"
kind: request
request: "[[Bitbucket - Get a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id} · Get a pull request. Returns the specified pull request. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
writes: false
expose: true
---
# bitbucket_get_a_pull_request

`GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}` — Get a pull request

- Request: [[Bitbucket - Get a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
