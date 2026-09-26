---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_move_resolutions
title: "Jira v3 - Move resolutions"
kind: request
request: "[[Jira v3 - Move resolutions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/resolution/move · Move resolutions. Changes the order of issue resolutions. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_move_resolutions

`PUT /rest/api/3/resolution/move` — Move resolutions

- Request: [[Jira v3 - Move resolutions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
