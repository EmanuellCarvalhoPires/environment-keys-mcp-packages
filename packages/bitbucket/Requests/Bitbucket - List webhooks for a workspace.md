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
path: "/workspaces/{workspace}/hooks"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_list_webhooks_for_a_workspace]]"
---
# Bitbucket - List webhooks for a workspace

**List webhooks for a workspace** — `GET /workspaces/{workspace}/hooks`

- Run by the tool [[bitbucket_list_webhooks_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/hooks
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns a paginated list of webhooks installed on this workspace.
