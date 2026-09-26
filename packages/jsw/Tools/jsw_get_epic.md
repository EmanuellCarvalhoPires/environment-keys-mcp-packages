---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_epic
title: "JSW - Get epic"
kind: request
request: "[[JSW - Get epic]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/epic/{epicIdOrKey} · Get epic. Returns the epic for a given epic ID. This epic will only be returned if the user has permission to view it. Note: This operation does not work for epics in next-gen projects. Writes data: no."
params:
  "epicIdOrKey":
    type: string
    required: true
    description: "The id or key of the requested epic."
writes: false
expose: false
---
# jsw_get_epic

`GET /rest/agile/1.0/epic/{epicIdOrKey}` — Get epic

- Request: [[JSW - Get epic]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
