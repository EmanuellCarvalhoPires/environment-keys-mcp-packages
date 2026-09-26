---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_pull_request
title: "Bitbucket - Update a pull request"
kind: request
request: "[[Bitbucket - Update a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id} · Update a pull request. Mutates the specified pull request. This can be used to change the pull request's branches or description. Only open pull requests can be mutated. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_pull_request

`PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}` — Update a pull request

- Request: [[Bitbucket - Update a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
