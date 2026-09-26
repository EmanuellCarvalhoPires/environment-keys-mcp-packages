---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branch-restrictions
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}"
category: "Branch restrictions"
writes_data: true
tool_note: "[[bitbucket_update_a_branch_restriction_rule]]"
---
# Bitbucket - Update a branch restriction rule

**Update a branch restriction rule** — `PUT /repositories/{workspace}/{repo_slug}/branch-restrictions/{id}`

- Run by the tool [[bitbucket_update_a_branch_restriction_rule]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/branch-restrictions/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates an existing branch restriction rule.

Fields not present in the request body are ignored.

See [`POST`](/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-post) for details.
