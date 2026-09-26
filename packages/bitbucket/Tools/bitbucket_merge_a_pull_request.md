---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_merge_a_pull_request
title: "Bitbucket - Merge a pull request"
kind: request
request: "[[Bitbucket - Merge a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge · Merge a pull request. Merges the pull request. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
  "async":
    type: string
    required: false
    description: "Default value is false. When set to true, runs merge asynchronously and immediately returns a 202 with polling link to the task-status API in the Location header."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_merge_a_pull_request

`POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge` — Merge a pull request

- Request: [[Bitbucket - Merge a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
