---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_list_tasks_on_a_pull_request]]"
---
# Bitbucket - List tasks on a pull request

**List tasks on a pull request** — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks`

- Run by the tool [[bitbucket_list_tasks_on_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/tasks?q={{param:q}}&sort={{param:sort}}&pagelen={{param:pagelen}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.
- `q` (query, string, optional) — Query string to narrow down the response. See filtering and sorting for details.
- `sort` (query, string, optional) — Field by which the results should be sorted as per filtering and sorting. Defaults to createdon.
- `pagelen` (query, string, optional) — Current number of objects on the existing page. The default value is 10 with 100 being the maximum allowed value. Individual APIs may enforce different values.

## Original description

Returns a paginated list of the pull request's tasks.

This endpoint supports filtering and sorting of the results by the 'task' field.
See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
