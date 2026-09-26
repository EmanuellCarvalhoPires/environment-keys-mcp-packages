---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/task
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/tasks"
category: "Task"
writes_data: false
tool_note: "[[confluence_get_tasks]]"
---
# Confluence v2 - Get tasks

**Get tasks** — `GET /tasks`

- Run by the tool [[confluence_get_tasks]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/tasks?body-format={{param:body_format}}&include-blank-tasks={{param:include_blank_tasks}}&status={{param:status}}&task-id={{param:task_id}}&space-id={{param:space_id}}&page-id={{param:page_id}}&blogpost-id={{param:blogpost_id}}&created-by={{param:created_by}}&assigned-to={{param:assigned_to}}&completed-by={{param:completed_by}}&created-at-from={{param:created_at_from}}&created-at-to={{param:created_at_to}}&due-at-from={{param:due_at_from}}&due-at-to={{param:due_at_to}}&completed-at-from={{param:completed_at_from}}&completed-at-to={{param:completed_at_to}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `include_blank_tasks` (query, string, optional) — Specifies whether to include blank tasks in the response. Defaults to true.
- `status` (query, string, optional) — Filters on the status of the task.
- `task_id` (query, string, optional) — Filters on task ID. Multiple IDs can be specified.
- `space_id` (query, string, optional) — Filters on the space ID of the task. Multiple IDs can be specified.
- `page_id` (query, string, optional) — Filters on the page ID of the task. Multiple IDs can be specified. Note - page and blog post filters can be used in conjunction.
- `blogpost_id` (query, string, optional) — Filters on the blog post ID of the task. Multiple IDs can be specified. Note - page and blog post filters can be used in conjunction.
- `created_by` (query, string, optional) — Filters on the Account ID of the user who created this task. Multiple IDs can be specified.
- `assigned_to` (query, string, optional) — Filters on the Account ID of the user to whom this task is assigned. Multiple IDs can be specified.
- `completed_by` (query, string, optional) — Filters on the Account ID of the user who completed this task. Multiple IDs can be specified.
- `created_at_from` (query, string, optional) — Filters on start of date-time range of task based on creation date (inclusive). Input is epoch time in milliseconds.
- `created_at_to` (query, string, optional) — Filters on end of date-time range of task based on creation date (inclusive). Input is epoch time in milliseconds.
- `due_at_from` (query, string, optional) — Filters on start of date-time range of task based on due date (inclusive). Input is epoch time in milliseconds.
- `due_at_to` (query, string, optional) — Filters on end of date-time range of task based on due date (inclusive). Input is epoch time in milliseconds.
- `completed_at_from` (query, string, optional) — Filters on start of date-time range of task based on completion date (inclusive). Input is epoch time in milliseconds.
- `completed_at_to` (query, string, optional) — Filters on end of date-time range of task based on completion date (inclusive). Input is epoch time in milliseconds.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of tasks per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.

## Original description

Returns all tasks. The number of results is limited by the `limit` parameter and additional results (if available)
will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
Only tasks that the user has permission to view will be returned.
