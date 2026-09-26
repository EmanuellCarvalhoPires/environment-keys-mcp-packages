---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/long-running-task
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/longtask"
category: "Long-running task"
writes_data: false
tool_note: "[[confluence_v1_get_long_running_tasks]]"
---
# Confluence v1 - Get long-running tasks

**Get long-running tasks** — `GET /wiki/rest/api/longtask`

- Run by the tool [[confluence_v1_get_long_running_tasks]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/longtask?key={{param:key}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `key` (query, string, optional) — The key of the tasks.
- `start` (query, string, optional) — The starting index of the returned tasks.
- `limit` (query, string, optional) — The maximum number of tasks to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns information about all active long-running tasks (e.g. space export),
such as how long each task has been running and the percentage of each task
that has completed.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
