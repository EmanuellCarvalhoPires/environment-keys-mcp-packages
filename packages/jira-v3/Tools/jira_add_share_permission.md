---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_add_share_permission
title: "Jira v3 - Add share permission"
kind: request
request: "[[Jira v3 - Add share permission]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/filter/{id}/permission · Add share permission. Add a share permissions to a filter. If you add a global share permission (one for all logged-in users or the public) it will overwrite all share permissions for the filter. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_add_share_permission

`POST /rest/api/3/filter/{id}/permission` — Add share permission

- Request: [[Jira v3 - Add share permission]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
