---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_share_permission
title: "Jira v3 - Delete share permission"
kind: request
request: "[[Jira v3 - Delete share permission]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/filter/{id}/permission/{permissionId} · Delete share permission. Deletes a share permission from a filter. Permissions required: Permission to access Jira and the user must own the filter. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter."
  "permissionId":
    type: string
    required: true
    description: "The ID of the share permission."
writes: true
expose: false
---
# jira_delete_share_permission

`DELETE /rest/api/3/filter/{id}/permission/{permissionId}` — Delete share permission

- Request: [[Jira v3 - Delete share permission]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
