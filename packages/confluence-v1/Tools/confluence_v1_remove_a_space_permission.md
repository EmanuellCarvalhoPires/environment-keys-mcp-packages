---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permissions
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_remove_a_space_permission
title: "Confluence v1 - Remove a space permission"
kind: request
request: "[[Confluence v1 - Remove a space permission]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/space/{spaceKey}/permission/{id} · Remove a space permission. Removes a space permission. Note that removing Read Space permission for a user or group will remove all the space permissions for that user or group. Note: Apps cannot access this REST resource - including when utilizing user impersonation. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to be queried for its content."
  "id":
    type: string
    required: true
    description: "Id of the permission to be deleted."
writes: true
expose: false
---
# confluence_v1_remove_a_space_permission

`DELETE /wiki/rest/api/space/{spaceKey}/permission/{id}` — Remove a space permission

- Request: [[Confluence v1 - Remove a space permission]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
