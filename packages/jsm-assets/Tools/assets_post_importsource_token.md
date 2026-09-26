---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_importsource_token
title: "Assets - POST importsource {importSourceId} token"
kind: request
request: "[[Assets - POST importsource {importSourceId} token]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /importsource/{importSourceId}/token · /importsource/{importSourceId}/token. Generate a Bearer token which can be used to authenticate against Assets /importsource/ APIs, to take actions against the specified import source. Writes data: yes."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
writes: true
expose: false
---
# assets_post_importsource_token

`POST /importsource/{importSourceId}/token` — /importsource/{importSourceId}/token

- Request: [[Assets - POST importsource {importSourceId} token]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
