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
path: "/repositories/{workspace}/{repo_slug}/default-reviewers"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_list_default_reviewers]]"
---
# Bitbucket - List default reviewers

**List default reviewers** — `GET /repositories/{workspace}/{repo_slug}/default-reviewers`

- Run by the tool [[bitbucket_list_default_reviewers]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/default-reviewers
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Returns the repository's default reviewers.

These are the users that are automatically added as reviewers on every
new pull request that is created. To obtain the repository's default reviewers
as well as the default reviewers inherited from the project, use the
[effective-default-reveiwers](#api-repositories-workspace-repo-slug-effective-default-reviewers-get) endpoint.
