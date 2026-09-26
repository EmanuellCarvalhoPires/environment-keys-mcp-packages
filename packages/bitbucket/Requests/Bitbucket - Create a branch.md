---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/refs/branches"
category: "Refs"
writes_data: true
tool_note: "[[bitbucket_create_a_branch]]"
---
# Bitbucket - Create a branch

**Create a branch** — `POST /repositories/{workspace}/{repo_slug}/refs/branches`

- Run by the tool [[bitbucket_create_a_branch]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/refs/branches
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Creates a new branch in the specified repository.

The payload of the POST should consist of a JSON document that
contains the name of the tag and the target hash.

```
curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \
-s -u seanfarley -X POST -H "Content-Type: application/json" \
-d '{
    "name" : "smf/create-feature",
    "target" : {
        "hash" : "default",
    }
}'
```

This call requires authentication. Private repositories require the
caller to authenticate with an account that has appropriate
authorization.

The branch name should not include any prefixes (e.g.
refs/heads). This endpoint does support using short hash prefixes for
the commit hash, but it may return a 400 response if the provided
prefix is ambiguous. Using a full commit hash is the preferred
approach.
