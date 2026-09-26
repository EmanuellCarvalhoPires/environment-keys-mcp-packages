---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_remove_a_user_from_the_default_reviewers]]"
---
# Bitbucket - Remove a user from the default reviewers

**Remove a user from the default reviewers** — `DELETE /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}`

- Run by the tool [[bitbucket_remove_a_user_from_the_default_reviewers]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/default-reviewers/{{param:target_username}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `target_username` (path, string, required) — Value of targetusername in the path.

## Original description

Removes a default reviewer from the repository.
