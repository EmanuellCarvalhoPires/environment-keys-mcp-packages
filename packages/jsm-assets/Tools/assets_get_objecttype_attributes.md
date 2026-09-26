---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_objecttype_attributes
title: "Assets - GET objecttype {id} attributes"
kind: request
request: "[[Assets - GET objecttype {id} attributes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /objecttype/{id}/attributes · /objecttype/{id}/attributes. Find all attributes for this object type Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
  "onlyValueEditable":
    type: string
    required: false
    description: "Query parameter onlyValueEditable."
  "orderByName":
    type: string
    required: false
    description: "Query parameter orderByName."
  "query":
    type: string
    required: false
    description: "Query parameter query."
  "includeValuesExist":
    type: string
    required: false
    description: "Query parameter includeValuesExist."
  "excludeParentAttributes":
    type: string
    required: false
    description: "Query parameter excludeParentAttributes."
  "includeChildren":
    type: string
    required: false
    description: "Query parameter includeChildren."
  "orderByRequired":
    type: string
    required: false
    description: "Query parameter orderByRequired."
writes: false
expose: false
---
# assets_get_objecttype_attributes

`GET /objecttype/{id}/attributes` — /objecttype/{id}/attributes

- Request: [[Assets - GET objecttype {id} attributes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
