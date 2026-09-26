---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_pull_requests_that_contain_a_commit
title: "Bitbucket - List pull requests that contain a commit"
kind: request
request: "[[Bitbucket - List pull requests that contain a commit]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests · List pull requests that contain a commit. Returns a paginated list of all pull requests as part of which this commit was reviewed. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository; either the UUID in curly braces, or the slug"
  "commit":
    type: string
    required: true
    description: "The SHA1 of the commit"
  "page":
    type: string
    required: false
    description: "Which page to retrieve"
  "pagelen":
    type: string
    required: false
    description: "How many pull requests to retrieve per page"
writes: false
expose: false
---
# bitbucket_list_pull_requests_that_contain_a_commit

`GET /repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests` — List pull requests that contain a commit

- Request: [[Bitbucket - List pull requests that contain a commit]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
