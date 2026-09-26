---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_report
title: "Bitbucket - Get a report"
kind: request
request: "[[Bitbucket - Get a report]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId} · Get a report. Returns a single Report matching the provided ID. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "commit":
    type: string
    required: true
    description: "The commit the report belongs to."
  "reportId":
    type: string
    required: true
    description: "Either the uuid or external-id of the report."
writes: false
expose: false
---
# bitbucket_get_a_report

`GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}` — Get a report

- Request: [[Bitbucket - Get a report]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
