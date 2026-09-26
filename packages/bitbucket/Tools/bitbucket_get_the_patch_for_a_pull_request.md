---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_patch_for_a_pull_request
title: "Bitbucket - Get the patch for a pull request"
kind: request
request: "[[Bitbucket - Get the patch for a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch · Get the patch for a pull request. Redirects to the repository patch with the revspec that corresponds to pull request. Writes data: no."
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
# bitbucket_get_the_patch_for_a_pull_request

`GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch` — Get the patch for a pull request

- Request: [[Bitbucket - Get the patch for a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
