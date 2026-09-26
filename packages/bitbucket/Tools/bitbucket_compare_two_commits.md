---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_compare_two_commits
title: "Bitbucket - Compare two commits"
kind: request
request: "[[Bitbucket - Compare two commits]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/diff/{spec} · Compare two commits. Produces a raw git-style diff. Single commit spec If the spec argument to this API is a single commit, the diff is produced against the first parent of the specified commit. Two commit spec Two commits separated by .. may be provided as the spec, e.g., 3a8b42..9ff173. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "spec":
    type: string
    required: true
    description: "Value of spec in the path."
  "context":
    type: string
    required: false
    description: "Generate diffs with lines of context instead of the usual three."
  "path":
    type: string
    required: false
    description: "Limit the diff to a particular file (this parameter can be repeated for multiple paths)."
  "ignore_whitespace":
    type: string
    required: false
    description: "Generate diffs that ignore whitespace."
  "binary":
    type: string
    required: false
    description: "Generate diffs that include binary files, true if omitted."
  "renames":
    type: string
    required: false
    description: "Whether to perform rename detection, true if omitted."
  "merge":
    type: string
    required: false
    description: "This parameter is deprecated. The 'topic' parameter should be used instead. The 'merge' and 'topic' parameters cannot be both used at the same time."
  "topic":
    type: string
    required: false
    description: "If true, returns 2-way 'three-dot' diff. This is a diff between the source commit and the merge base of the source commit and the destination commit."
writes: false
expose: false
---
# bitbucket_compare_two_commits

`GET /repositories/{workspace}/{repo_slug}/diff/{spec}` — Compare two commits

- Request: [[Bitbucket - Compare two commits]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
