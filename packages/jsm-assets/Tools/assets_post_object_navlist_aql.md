---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/search
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_post_object_navlist_aql
title: "Assets - POST object navlist aql"
kind: request
request: "[[Assets - POST object navlist aql]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /object/navlist/aql · /object/navlist/aql. Retrieve a list of objects based on an AQL. Deprecated from 30 September 2024. Please use POST /object/aql instead. For more information please see https://developer.atlassian.com/changelog/CHANGE-1661. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# assets_post_object_navlist_aql

`POST /object/navlist/aql` — /object/navlist/aql

- Request: [[Assets - POST object navlist aql]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
