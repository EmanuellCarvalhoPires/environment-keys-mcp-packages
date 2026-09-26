---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_a_commit_s_comments
title: "Bitbucket - List a commit's comments"
kind: request
request: "[[Bitbucket - List a commit's comments]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments · List a commit's comments. Returns the commit's comments. This includes both global and inline comments. The default sorting is oldest to newest and can be overridden with the sort query parameter. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
  "q":
    type: string
    required: false
    description: "Query string to narrow down the response as per filtering and sorting."
  "sort":
    type: string
    required: false
    description: "Field by which the results should be sorted as per filtering and sorting."
writes: false
expose: false
---
# bitbucket_list_a_commit_s_comments

`GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments` — List a commit's comments

- Request: [[Bitbucket - List a commit's comments]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
