---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_ssh_key_pair]]"
---
# Bitbucket - Get SSH key pair

**Get SSH key pair** — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair`

- Run by the tool [[bitbucket_get_ssh_key_pair]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/ssh/key_pair
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.

## Original description

Retrieve the repository SSH key pair excluding the SSH private key. The private key is a write only field and will never be exposed in the logs or the REST API.
