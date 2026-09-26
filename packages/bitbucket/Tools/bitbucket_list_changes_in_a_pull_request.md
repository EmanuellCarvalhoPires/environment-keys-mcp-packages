---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_changes_in_a_pull_request
title: "Bitbucket - List changes in a pull request"
kind: request
request: "[[Bitbucket - List changes in a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff · List changes in a pull request. Redirects to the repository diff with the revspec that corresponds to the pull request. Writes data: no."
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
# bitbucket_list_changes_in_a_pull_request

`GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff` — List changes in a pull request

- Request: [[Bitbucket - List changes in a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
