---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branch-restrictions
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}"
category: "Branch restrictions"
writes_data: false
tool_note: "[[bitbucket_get_a_branch_restriction_rule]]"
---
# Bitbucket - Get a branch restriction rule

**Get a branch restriction rule** — `GET /repositories/{workspace}/{repo_slug}/branch-restrictions/{id}`

- Run by the tool [[bitbucket_get_a_branch_restriction_rule]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/branch-restrictions/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `id` (path, string, required) — Value of id in the path.

## Original description

Returns a specific branch restriction rule.
