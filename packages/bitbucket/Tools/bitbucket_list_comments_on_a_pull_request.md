---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_comments_on_a_pull_request
title: "Bitbucket - List comments on a pull request"
kind: request
request: "[[Bitbucket - List comments on a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments · List comments on a pull request. Returns a paginated list of the pull request's comments. This includes both global, inline comments and replies. The default sorting is oldest to newest and can be overridden with the sort query parameter. This endpoint also supports filtering and sorting of the results. Writes data: no."
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
expose: false
---
# bitbucket_list_comments_on_a_pull_request

`GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments` — List comments on a pull request

- Request: [[Bitbucket - List comments on a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
