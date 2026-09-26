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
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_list_commit_statuses_for_a_pull_request]]"
---
# Bitbucket - List commit statuses for a pull request

**List commit statuses for a pull request** — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses`

- Run by the tool [[bitbucket_list_commit_statuses_for_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/statuses?q={{param:q}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.
- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.
- `sort` (query, string, optional) — Field by which the results should be sorted as per filtering and sorting. Defaults to createdon.

## Original description

Returns all statuses (e.g. build results) for the given pull
request.
