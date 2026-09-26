---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commit-statuses
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_commit_statuses_for_a_commit
title: "Bitbucket - List commit statuses for a commit"
kind: request
request: "[[Bitbucket - List commit statuses for a commit]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses · List commit statuses for a commit. Returns all statuses (e.g. build results) for a specific commit. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
  "refname":
    type: string
    required: false
    description: "If specified, only return commit status objects that were either created without a refname, or were created with the specified refname"
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
# bitbucket_list_commit_statuses_for_a_commit

`GET /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses` — List commit statuses for a commit

- Request: [[Bitbucket - List commit statuses for a commit]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
