---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_objectschema_list
title: "Assets - GET objectschema list"
kind: request
request: "[[Assets - GET objectschema list]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /objectschema/list · /objectschema/list. Resource to find object schemas in Assets Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The starting index for the next page of results"
  "maxResults":
    type: string
    required: false
    description: "The maximum number of objects to return in this page of results. Actual number of results may be less, for example, if the last page of results is returned."
  "includeCounts":
    type: string
    required: false
    description: "Should the object and object type count for schema be included in the response. If this parameter is false, object and object type count will return 0."
writes: false
expose: true
---
# assets_get_objectschema_list

`GET /objectschema/list` — /objectschema/list

- Request: [[Assets - GET objectschema list]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
