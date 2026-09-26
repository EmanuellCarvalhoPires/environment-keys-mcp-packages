---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_approve_a_pull_request
title: "Bitbucket - Approve a pull request"
kind: request
request: "[[Bitbucket - Approve a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve · Approve a pull request. Approve the specified pull request as the authenticated user. Writes data: yes."
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
# bitbucket_approve_a_pull_request

`POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve` — Approve a pull request

- Request: [[Bitbucket - Approve a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
