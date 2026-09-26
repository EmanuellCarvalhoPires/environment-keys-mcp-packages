---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_unapprove_a_pull_request
title: "Bitbucket - Unapprove a pull request"
kind: request
request: "[[Bitbucket - Unapprove a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve · Unapprove a pull request. Redact the authenticated user's approval of the specified pull request. Writes data: yes."
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
# bitbucket_unapprove_a_pull_request

`DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve` — Unapprove a pull request

- Request: [[Bitbucket - Unapprove a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
