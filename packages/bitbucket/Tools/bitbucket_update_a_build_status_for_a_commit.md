---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commit-statuses
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_build_status_for_a_commit
title: "Bitbucket - Update a build status for a commit"
kind: request
request: "[[Bitbucket - Update a build status for a commit]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key} · Update a build status for a commit. Used to update the current status of a build status object on the specific commit. This operation can also be used to change other properties of the build status: state name description url refname The key cannot be changed. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
  "key":
    type: string
    required: true
    description: "Value of key in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_build_status_for_a_commit

`PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}` — Update a build status for a commit

- Request: [[Bitbucket - Update a build status for a commit]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
