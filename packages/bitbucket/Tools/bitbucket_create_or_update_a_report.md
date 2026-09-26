---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_or_update_a_report
title: "Bitbucket - Create or update a report"
kind: request
request: "[[Bitbucket - Create or update a report]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId} · Create or update a report. Creates or updates a report for the specified commit. To upload a report, make sure to generate an ID that is unique across all reports for that commit. Writes data: yes."
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
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_or_update_a_report

`PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}` — Create or update a report

- Request: [[Bitbucket - Create or update a report]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
