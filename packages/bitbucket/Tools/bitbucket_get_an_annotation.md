---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_an_annotation
title: "Bitbucket - Get an annotation"
kind: request
request: "[[Bitbucket - Get an annotation]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId} · Get an annotation. Returns a single Annotation matching the provided ID. Writes data: no."
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
writes: false
expose: false
---
# bitbucket_get_an_annotation

`GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}` — Get an annotation

- Request: [[Bitbucket - Get an annotation]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
