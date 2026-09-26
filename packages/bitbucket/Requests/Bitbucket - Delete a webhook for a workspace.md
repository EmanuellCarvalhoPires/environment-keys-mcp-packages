---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/workspaces/{workspace}/hooks/{uid}"
category: "Workspaces"
writes_data: true
tool_note: "[[bitbucket_delete_a_webhook_for_a_workspace]]"
---
# Bitbucket - Delete a webhook for a workspace

**Delete a webhook for a workspace** — `DELETE /workspaces/{workspace}/hooks/{uid}`

- Run by the tool [[bitbucket_delete_a_webhook_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/workspaces/{{service.workspace}}/hooks/{{param:uid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `uid` (path, string, required) — Value of uid in the path.

## Original description

Deletes the specified webhook subscription from the given workspace.
