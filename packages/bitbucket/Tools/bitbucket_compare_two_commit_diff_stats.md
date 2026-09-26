---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_compare_two_commit_diff_stats
title: "Bitbucket - Compare two commit diff stats"
kind: request
request: "[[Bitbucket - Compare two commit diff stats]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/diffstat/{spec} · Compare two commit diff stats. Produces a response in JSON format with a record for every path modified, including information on the type of the change and the number of lines added and removed. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "spec":
    type: string
    required: true
    description: "Value of spec in the path."
writes: false
expose: false
---
# bitbucket_compare_two_commit_diff_stats

`GET /repositories/{workspace}/{repo_slug}/diffstat/{spec}` — Compare two commit diff stats

- Request: [[Bitbucket - Compare two commit diff stats]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
