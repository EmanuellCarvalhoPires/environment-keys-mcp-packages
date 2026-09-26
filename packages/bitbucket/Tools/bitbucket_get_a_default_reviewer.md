---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_default_reviewer
title: "Bitbucket - Get a default reviewer"
kind: request
request: "[[Bitbucket - Get a default reviewer]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user} · Get a default reviewer. Returns the specified default reviewer. Writes data: no."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
writes: false
expose: false
---
# bitbucket_get_a_default_reviewer

`GET /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}` — Get a default reviewer

- Request: [[Bitbucket - Get a default reviewer]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
