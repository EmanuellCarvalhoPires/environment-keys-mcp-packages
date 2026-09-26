---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/search
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_post_object_aql
title: "Assets - POST object aql"
kind: request
request: "[[Assets - POST object aql]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /object/aql · /object/aql. Fetch Objects by AQL Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The starting index for the next page of results"
  "maxResults":
    type: string
    required: false
    description: "The maximum number of objects to return in this page of results. Actual number of results may be less, for example, if the last page of results is returned."
  "includeAttributes":
    type: string
    required: false
    description: "Should the objects attributes be included in the response. If this parameter is false only the information on the object will be returned and the object attributes will not be present"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: true
---
# assets_post_object_aql

`POST /object/aql` — /object/aql

- Request: [[Assets - POST object aql]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
