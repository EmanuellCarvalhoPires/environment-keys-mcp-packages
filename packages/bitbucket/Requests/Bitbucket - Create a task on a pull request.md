---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_create_a_task_on_a_pull_request]]"
---
# Bitbucket - Create a task on a pull request

**Create a task on a pull request** — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks`

- Run by the tool [[bitbucket_create_a_task_on_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/tasks
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new pull request task.

Returns the newly created pull request task.

Tasks can optionally be created in relation to a comment specified by the comment's ID which
will cause the task to appear below the comment on a pull request when viewed in Bitbucket.
