---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/config/statustype"
category: "Config"
writes_data: true
tool_note: "[[assets_post_config_statustype]]"
---
# Assets - POST config statustype

**/config/statustype** — `POST /config/statustype`

- Run by the tool [[assets_post_config_statustype]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/config/statustype
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "name": "Decommissioned",
  "category": 0,
  "objectSchemaId": "6"
}
```

## Original description

Create a new status
