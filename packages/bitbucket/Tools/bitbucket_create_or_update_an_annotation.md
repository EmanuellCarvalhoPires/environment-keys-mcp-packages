---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_or_update_an_annotation
title: "Bitbucket - Create or update an annotation"
kind: request
request: "[[Bitbucket - Create or update an annotation]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId} · Create or update an annotation. Creates or updates an individual annotation for the specified report. Annotations are individual findings that have been identified as part of a report, for example, a line of code that represents a vulnerability. Writes data: yes."
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
  "annotationId":
    type: string
    required: true
    description: "Either the uuid or external-id of the annotation."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_or_update_an_annotation

`PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}` — Create or update an annotation

- Request: [[Bitbucket - Create or update an annotation]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
