---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/source
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_commits_that_modified_a_file
title: "Bitbucket - List commits that modified a file"
kind: request
request: "[[Bitbucket - List commits that modified a file]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path} · List commits that modified a file. Returns a paginated list of commits that modified the specified file. Commits are returned in reverse chronological order. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
  "path":
    type: string
    required: true
    description: "Value of path in the path."
  "renames":
    type: string
    required: false
    description: "When true, Bitbucket will follow the history of the file across renames (this is the default behavior). This can be turned off by specifying false."
  "q":
    type: string
    required: false
    description: "Query string to narrow down the response as per filtering and sorting."
  "sort":
    type: string
    required: false
    description: "Name of a response property sort the result by as per filtering and sorting."
writes: false
expose: false
---
# bitbucket_list_commits_that_modified_a_file

`GET /repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}` — List commits that modified a file

- Request: [[Bitbucket - List commits that modified a file]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
