---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/long-running-task
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/longtask/{id}"
category: "Long-running task"
writes_data: false
tool_note: "[[confluence_v1_get_long_running_task]]"
---
# Confluence v1 - Get long-running task

**Get long-running task** — `GET /wiki/rest/api/longtask/{id}`

- Run by the tool [[confluence_v1_get_long_running_task]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/longtask/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the task.

## Original description

Returns information about an active long-running task (e.g. space export),
such as how long it has been running and the percentage of the task that
has completed.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
