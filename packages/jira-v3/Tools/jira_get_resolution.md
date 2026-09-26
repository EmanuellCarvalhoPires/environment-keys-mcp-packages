---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_resolution
title: "Jira v3 - Get resolution"
kind: request
request: "[[Jira v3 - Get resolution]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/resolution/{id} · Get resolution. Returns an issue resolution value. Permissions required: Permission to access Jira. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue resolution value."
writes: false
expose: false
---
# jira_get_resolution

`GET /rest/api/3/resolution/{id}` — Get resolution

- Request: [[Jira v3 - Get resolution]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
