---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/priority-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_priority_scheme
title: "Jira v3 - Update priority scheme"
kind: request
request: "[[Jira v3 - Update priority scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/priorityscheme/{schemeId} · Update priority scheme. Updates a priority scheme. This includes its details, the lists of priorities and projects in it Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the priority scheme."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_priority_scheme

`PUT /rest/api/3/priorityscheme/{schemeId}` — Update priority scheme

- Request: [[Jira v3 - Update priority scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
