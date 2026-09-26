---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permission-transition
  - api/operation/get
  - api/effect/read
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/space-permissions/transition/tasks/{taskId}"
category: "Space Permission Transition"
writes_data: false
tool_note: "[[confluence_get_space_permission_transition_task_status]]"
---
# Confluence v2 - Get space permission transition task status

**Get space permission transition task status** — `GET /space-permissions/transition/tasks/{taskId}`

- Run by the tool [[confluence_get_space_permission_transition_task_status]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/space-permissions/transition/tasks/{{param:taskId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `taskId` (path, string, required) — The ID of the async task, as returned by the generate-combinations, assign-roles, or remove-access endpoints.

## Original description

Retrieves the status of an async space permission transition task. Use the taskId returned
from the generate-combinations, assign-roles, or remove-access endpoints to poll for
progress and completion.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be a Confluence administrator.
