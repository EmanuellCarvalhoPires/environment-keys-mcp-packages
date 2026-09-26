---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_share_permission
title: "Jira v3 - Get share permission"
kind: request
request: "[[Jira v3 - Get share permission]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/filter/{id}/permission/{permissionId} · Get share permission. Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission. This operation can be accessed anonymously. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter."
  "permissionId":
    type: string
    required: true
    description: "The ID of the share permission."
writes: false
expose: false
---
# jira_get_share_permission

`GET /rest/api/3/filter/{id}/permission/{permissionId}` — Get share permission

- Request: [[Jira v3 - Get share permission]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
