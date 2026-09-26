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
path: "/config/referencetype"
category: "Config"
writes_data: true
tool_note: "[[assets_post_config_referencetype]]"
---
# Assets - POST config referencetype

**/config/referencetype** — `POST /config/referencetype`

- Run by the tool [[assets_post_config_referencetype]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/config/referencetype
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "name": "Depends on",
  "description": "",
  "color": "42526E",
  "objectSchemaId": "27"
}
```

## Original description

Update a reference type
