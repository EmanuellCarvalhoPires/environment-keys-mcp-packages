---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/task
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/tasks/{id}"
category: "Task"
writes_data: false
tool_note: "[[confluence_get_task_by_id]]"
---
# Confluence v2 - Get task by id

**Get task by id** — `GET /tasks/{id}`

- Run by the tool [[confluence_get_task_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/tasks/{{param:id}}?body-format={{param:body_format}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the task to be returned. If you don't know the task ID, use Get tasks and filter the results.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.

## Original description

Returns a specific task. 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the containing page or blog post and its corresponding space.
