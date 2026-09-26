---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_file_conflicts_for_a_commit_spec
title: "Bitbucket - Get file conflicts for a commit spec"
kind: request
request: "[[Bitbucket - Get file conflicts for a commit spec]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/file-conflicts/{spec} · Get file conflicts for a commit spec. Get file conflicts for a commit spec Writes data: no."
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
# bitbucket_get_file_conflicts_for_a_commit_spec

`GET /repositories/{workspace}/{repo_slug}/file-conflicts/{spec}` — Get file conflicts for a commit spec

- Request: [[Bitbucket - Get file conflicts for a commit spec]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
