---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branch-restrictions
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}"
category: "Branch restrictions"
writes_data: true
tool_note: "[[bitbucket_delete_a_branch_restriction_rule]]"
---
# Bitbucket - Delete a branch restriction rule

**Delete a branch restriction rule** — `DELETE /repositories/{workspace}/{repo_slug}/branch-restrictions/{id}`

- Run by the tool [[bitbucket_delete_a_branch_restriction_rule]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/branch-restrictions/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `id` (path, string, required) — Value of id in the path.

## Original description

Deletes an existing branch restriction rule.
