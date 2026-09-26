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
tool: jira_update_resolution
title: "Jira v3 - Update resolution"
kind: request
request: "[[Jira v3 - Update resolution]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/resolution/{id} · Update resolution. Updates an issue resolution. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue resolution."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_resolution

`PUT /rest/api/3/resolution/{id}` — Update resolution

- Request: [[Jira v3 - Update resolution]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
