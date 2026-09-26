---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_rank_epics
title: "JSW - Rank epics"
kind: request
request: "[[JSW - Rank epics]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · PUT /rest/agile/1.0/epic/{epicIdOrKey}/rank · Rank epics. Moves (ranks) an epic before or after a given epic. If rankCustomFieldId is not defined, the default rank field will be used. Note: This operation does not work for epics in next-gen projects. Writes data: yes."
params:
  "epicIdOrKey":
    type: string
    required: true
    description: "The id or key of the epic to rank."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_rank_epics

`PUT /rest/agile/1.0/epic/{epicIdOrKey}/rank` — Rank epics

- Request: [[JSW - Rank epics]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
