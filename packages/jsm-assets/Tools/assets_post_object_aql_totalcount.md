---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/search
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_post_object_aql_totalcount
title: "Assets - POST object aql totalcount"
kind: request
request: "[[Assets - POST object aql totalcount]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /object/aql/totalcount · /object/aql/totalcount. This API provides the total count of objects that match a specified AQL query. Please note that this operation may incur performance latency. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# assets_post_object_aql_totalcount

`POST /object/aql/totalcount` — /object/aql/totalcount

- Request: [[Assets - POST object aql totalcount]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
