---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_partially_update_epic
title: "JSW - Partially update epic"
kind: request
request: "[[JSW - Partially update epic]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/epic/{epicIdOrKey} · Partially update epic. Performs a partial update of the epic. A partial update means that fields not present in the request JSON will not be updated. Valid values for color are color1 to color9. Note: This operation does not work for epics in next-gen projects. Writes data: yes."
params:
  "epicIdOrKey":
    type: string
    required: true
    description: "The id or key of the epic to update."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_partially_update_epic

`POST /rest/agile/1.0/epic/{epicIdOrKey}` — Partially update epic

- Request: [[JSW - Partially update epic]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
