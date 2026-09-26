---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_decline_a_pull_request
title: "Bitbucket - Decline a pull request"
kind: request
request: "[[Bitbucket - Decline a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline · Decline a pull request. Declines the pull request. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
writes: true
expose: false
---
# bitbucket_decline_a_pull_request

`POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline` — Decline a pull request

- Request: [[Bitbucket - Decline a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
