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
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_list_pull_requests_that_contain_a_commit]]"
---
# Bitbucket - List pull requests that contain a commit

**List pull requests that contain a commit** — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests`

- Run by the tool [[bitbucket_list_pull_requests_that_contain_a_commit]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/pullrequests?page={{param:page}}&pagelen={{param:pagelen}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository; either the UUID in curly braces, or the slug
- `commit` (path, string, required) — The SHA1 of the commit
- `page` (query, string, optional) — Which page to retrieve
- `pagelen` (query, string, optional) — How many pull requests to retrieve per page

## Original description

Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull Request Commit Links app must be installed first before using this API; installation automatically occurs when 'Go to pull request' is clicked from the web interface for a commit's details.
