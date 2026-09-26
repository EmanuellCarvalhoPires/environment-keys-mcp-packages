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
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_list_commits_on_a_pull_request]]"
---
# Bitbucket - List commits on a pull request

**List commits on a pull request** — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits`

- Run by the tool [[bitbucket_list_commits_on_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/commits
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.

## Original description

Returns a paginated list of the pull request's commits.

These are the commits that are being merged into the destination
branch when the pull requests gets accepted.
