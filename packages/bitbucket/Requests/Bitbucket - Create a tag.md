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
path: "/repositories/{workspace}/{repo_slug}/refs/tags"
category: "Refs"
writes_data: true
tool_note: "[[bitbucket_create_a_tag]]"
---
# Bitbucket - Create a tag

**Create a tag** — `POST /repositories/{workspace}/{repo_slug}/refs/tags`

- Run by the tool [[bitbucket_create_a_tag]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/refs/tags
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new annotated tag in the specified repository.

The payload of the POST should consist of a JSON document that
contains the name of the tag and the target hash.

```
curl https://api.bitbucket.org/2.0/repositories/jdoe/myrepo/refs/tags \
-s -u jdoe -X POST -H "Content-Type: application/json" \
-d '{
    "name" : "new-tag-name",
    "target" : {
        "hash" : "a1b2c3d4e5f6",
    }
}'
```

This endpoint does support using short hash prefixes for the commit
hash, but it may return a 400 response if the provided prefix is
ambiguous. Using a full commit hash is the preferred approach.

A message for the tag object may optionally be provided. If it is
omitted or the provided message is empty, a default message of
"Added tag  for changeset " will be used.
