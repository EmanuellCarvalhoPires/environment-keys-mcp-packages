---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_an_annotation
title: "Bitbucket - Delete an annotation"
kind: request
request: "[[Bitbucket - Delete an annotation]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId} · Delete an annotation. Deletes a single Annotation matching the provided ID. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "commit":
    type: string
    required: true
    description: "The commit the annotation belongs to."
  "reportId":
    type: string
    required: true
    description: "Either the uuid or external-id of the annotation."
  "annotationId":
    type: string
    required: true
    description: "Either the uuid or external-id of the annotation."
writes: true
expose: false
---
# bitbucket_delete_an_annotation

`DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}` — Delete an annotation

- Request: [[Bitbucket - Delete an annotation]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
