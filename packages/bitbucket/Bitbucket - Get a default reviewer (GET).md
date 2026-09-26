---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_get_a_default_reviewer_get]]"
---
# Bitbucket - Get a default reviewer (GET)

**Get a default reviewer** — `GET /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}`

- Run by the tool [[bitbucket_get_a_default_reviewer_get]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/default-reviewers/{{param:target_username}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `target_username` (path, string, required) — Value of targetusername in the path.

## Original description

Returns the specified reviewer.

This can be used to test whether a user is among the repository's
default reviewers list. A 404 indicates that that specified user is not
a default reviewer.
