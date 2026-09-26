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
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_get_the_diff_stat_for_a_pull_request]]"
---
# Bitbucket - Get the diff stat for a pull request

**Get the diff stat for a pull request** — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat`

- Run by the tool [[bitbucket_get_the_diff_stat_for_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/diffstat
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.

## Original description

Redirects to the [repository diffstat](/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-diffstat-spec-get)
with the revspec that corresponds to the pull request.
