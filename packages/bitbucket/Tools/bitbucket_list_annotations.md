---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_annotations
title: "Bitbucket - List annotations"
kind: request
request: "[[Bitbucket - List annotations]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations · List annotations. Returns a paginated list of Annotations for a specified report. Writes data: no."
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
writes: false
expose: false
---
# bitbucket_list_annotations

`GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations` — List annotations

- Request: [[Bitbucket - List annotations]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
