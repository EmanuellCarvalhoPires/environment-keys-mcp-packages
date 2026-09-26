---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_bulk_create_or_update_annotations
title: "Bitbucket - Bulk create or update annotations"
kind: request
request: "[[Bitbucket - Bulk create or update annotations]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations · Bulk create or update annotations. Bulk upload of annotations. Annotations are individual findings that have been identified as part of a report, for example, a line of code that represents a vulnerability. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "commit":
    type: string
    required: true
    description: "The commit for which to retrieve reports."
  "reportId":
    type: string
    required: true
    description: "Uuid or external-if of the report for which to get annotations for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_bulk_create_or_update_annotations

`POST /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations` — Bulk create or update annotations

- Request: [[Bitbucket - Bulk create or update annotations]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
