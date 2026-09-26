---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/hooks/{uid}"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_get_a_webhook_for_a_workspace]]"
---
# Bitbucket - Get a webhook for a workspace

**Get a webhook for a workspace** — `GET /workspaces/{workspace}/hooks/{uid}`

- Run by the tool [[bitbucket_get_a_webhook_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/hooks/{{param:uid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `uid` (path, string, required) — Value of uid in the path.

## Original description

Returns the webhook with the specified id installed on the given
workspace.
