---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_update_ssh_key_pair]]"
---
# Bitbucket - Update SSH key pair

**Update SSH key pair** — `PUT /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair`

- Run by the tool [[bitbucket_update_ssh_key_pair]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/ssh/key_pair
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create or update the repository SSH key pair. The private key will be set as a default SSH identity in your build container.
