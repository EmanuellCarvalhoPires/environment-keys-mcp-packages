---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_reports
title: "Bitbucket - List reports"
kind: request
request: "[[Bitbucket - List reports]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports · List reports. Returns a paginated list of Reports linked to this commit. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "commit":
    type: string
    required: true
    description: "The commit for which to retrieve reports."
writes: false
expose: false
---
# bitbucket_list_reports

`GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports` — List reports

- Request: [[Bitbucket - List reports]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
