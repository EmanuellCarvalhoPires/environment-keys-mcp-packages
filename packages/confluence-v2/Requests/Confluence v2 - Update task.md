---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/task
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/tasks/{id}"
category: "Task"
writes_data: true
tool_note: "[[confluence_update_task]]"
---
# Confluence v2 - Update task

**Update task** — `PUT /tasks/{id}`

- Run by the tool [[confluence_update_task]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/tasks/{{param:id}}?body-format={{param:body_format}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the task to be updated. If you don't know the task ID, use Get tasks and filter the results.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a task by id. This endpoint currently only supports updating task status.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the containing page or blog post and view its corresponding space.
