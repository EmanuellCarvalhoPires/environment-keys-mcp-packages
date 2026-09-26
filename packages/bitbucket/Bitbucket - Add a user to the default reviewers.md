---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_add_a_user_to_the_default_reviewers]]"
---
# Bitbucket - Add a user to the default reviewers

**Add a user to the default reviewers** — `PUT /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}`

- Run by the tool [[bitbucket_add_a_user_to_the_default_reviewers]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/default-reviewers/{{param:target_username}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `target_username` (path, string, required) — Value of targetusername in the path.

## Original description

Adds the specified user to the repository's list of default
reviewers.

This method is idempotent. Adding a user a second time has no effect.
