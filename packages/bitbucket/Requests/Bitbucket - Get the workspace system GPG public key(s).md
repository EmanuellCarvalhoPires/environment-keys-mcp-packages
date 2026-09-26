---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/settings/gpg/public-key"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_get_the_workspace_system_gpg_public_key_s]]"
---
# Bitbucket - Get the workspace system GPG public key(s)

**Get the workspace system GPG public key(s)** — `GET /workspaces/{workspace}/settings/gpg/public-key`

- Run by the tool [[bitbucket_get_the_workspace_system_gpg_public_key_s]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/settings/gpg/public-key
Authorization: {{service.auth_token}}
```

## Original description

Returns the system public GPG key(s). In most cases a single key is returned.
During a key rotation period, two keys may be returned.
