---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/importsource/{importSourceId}/token"
category: "Importsource"
writes_data: true
tool_note: "[[assets_post_importsource_token]]"
---
# Assets - POST importsource {importSourceId} token

**/importsource/{importSourceId}/token** — `POST /importsource/{importSourceId}/token`

- Run by the tool [[assets_post_importsource_token]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/token
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.

## Original description

Generate a Bearer token which can be used to authenticate against Assets `/importsource/` APIs, to take actions against the specified import source.
