---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/refs/tags/{name}"
category: "Refs"
writes_data: true
tool_note: "[[bitbucket_delete_a_tag]]"
---
# Bitbucket - Delete a tag

**Delete a tag** — `DELETE /repositories/{workspace}/{repo_slug}/refs/tags/{name}`

- Run by the tool [[bitbucket_delete_a_tag]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/refs/tags/{{param:name}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `name` (path, string, required) — Value of name in the path.

## Original description

Delete a tag in the specified repository.

The tag name should not include any prefixes (e.g. refs/tags).
