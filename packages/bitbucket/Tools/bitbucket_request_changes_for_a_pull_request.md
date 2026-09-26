---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_request_changes_for_a_pull_request
title: "Bitbucket - Request changes for a pull request"
kind: request
request: "[[Bitbucket - Request changes for a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes · Request changes for a pull request. Writes data: yes."
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
# bitbucket_request_changes_for_a_pull_request

`POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes` — Request changes for a pull request

- Request: [[Bitbucket - Request changes for a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
