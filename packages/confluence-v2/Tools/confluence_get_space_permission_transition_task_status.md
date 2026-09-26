---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permission-transition
  - api/operation/get
  - api/effect/read
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
tool: confluence_get_space_permission_transition_task_status
title: "Confluence v2 - Get space permission transition task status"
kind: request
request: "[[Confluence v2 - Get space permission transition task status]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /space-permissions/transition/tasks/{taskId} · Get space permission transition task status. Retrieves the status of an async space permission transition task. Use the taskId returned from the generate-combinations, assign-roles, or remove-access endpoints to poll for progress and completion. Permissions required: User must be a Confluence administrator. Writes data: no."
params:
  "taskId":
    type: string
    required: true
    description: "The ID of the async task, as returned by the generate-combinations, assign-roles, or remove-access endpoints."
writes: false
expose: false
---
# confluence_get_space_permission_transition_task_status

`GET /space-permissions/transition/tasks/{taskId}` — Get space permission transition task status

- Request: [[Confluence v2 - Get space permission transition task status]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
