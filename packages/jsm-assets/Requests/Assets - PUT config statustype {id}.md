---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: PUT
path: "/config/statustype/{id}"
category: "Config"
writes_data: true
tool_note: "[[assets_update_config_statustype]]"
---
# Assets - PUT config statustype {id}

**/config/statustype/{id}** — `PUT /config/statustype/{id}`

- Run by the tool [[assets_update_config_statustype]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
PUT https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/config/statustype/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
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

Update an existing status
