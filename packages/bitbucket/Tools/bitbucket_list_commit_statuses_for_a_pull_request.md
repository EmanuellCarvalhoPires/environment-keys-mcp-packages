---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_commit_statuses_for_a_pull_request
title: "Bitbucket - List commit statuses for a pull request"
kind: request
request: "[[Bitbucket - List commit statuses for a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses · List commit statuses for a pull request. Returns all statuses (e.g. build results) for the given pull request. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
  "q":
    type: string
    required: false
    description: "Query string to narrow down the response as per filtering and sorting."
  "sort":
    type: string
    required: false
    description: "Field by which the results should be sorted as per filtering and sorting. Defaults to createdon."
writes: false
expose: false
---
# bitbucket_list_commit_statuses_for_a_pull_request

`GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses` — List commit statuses for a pull request

- Request: [[Bitbucket - List commit statuses for a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
