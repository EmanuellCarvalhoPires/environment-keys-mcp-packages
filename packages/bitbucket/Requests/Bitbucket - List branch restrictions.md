---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branch-restrictions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/branch-restrictions"
category: "Branch restrictions"
writes_data: false
tool_note: "[[bitbucket_list_branch_restrictions]]"
---
# Bitbucket - List branch restrictions

**List branch restrictions** — `GET /repositories/{workspace}/{repo_slug}/branch-restrictions`

- Run by the tool [[bitbucket_list_branch_restrictions]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/branch-restrictions?kind={{param:kind}}&pattern={{param:pattern}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `kind` (query, string, optional) — Branch restrictions of this type
- `pattern` (query, string, optional) — Branch restrictions applied to branches of this pattern

## Original description

Returns a paginated list of all branch restrictions on the
repository.
