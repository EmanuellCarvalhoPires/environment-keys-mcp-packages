---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_report
title: "Bitbucket - Delete a report"
kind: request
request: "[[Bitbucket - Delete a report]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId} · Delete a report. Deletes a single Report matching the provided ID. Writes data: yes."
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
writes: true
expose: false
---
# bitbucket_delete_a_report

`DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}` — Delete a report

- Request: [[Bitbucket - Delete a report]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
