---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectconnectedtickets
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_objectconnectedtickets_tickets
title: "Assets - GET objectconnectedtickets {objectId} tickets"
kind: request
request: "[[Assets - GET objectconnectedtickets {objectId} tickets]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /objectconnectedtickets/{objectId}/tickets · /objectconnectedtickets/{objectId}/tickets. Relation between Jira issues and Assets objects Writes data: no."
params:
  "objectId":
    type: string
    required: true
    description: "Value of objectId in the path."
writes: false
expose: false
---
# assets_get_objectconnectedtickets_tickets

`GET /objectconnectedtickets/{objectId}/tickets` — /objectconnectedtickets/{objectId}/tickets

- Request: [[Assets - GET objectconnectedtickets {objectId} tickets]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
