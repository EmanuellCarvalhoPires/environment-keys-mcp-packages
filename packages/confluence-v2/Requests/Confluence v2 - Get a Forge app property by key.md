---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/app-properties
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/app/properties/{propertyKey}"
category: "App Properties"
writes_data: false
tool_note: "[[confluence_get_a_forge_app_property_by_key]]"
---
# Confluence v2 - Get a Forge app property by key

**Get a Forge app property by key.** — `GET /app/properties/{propertyKey}`

- Run by the tool [[confluence_get_a_forge_app_property_by_key]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/app/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `propertyKey` (path, string, required) — The key of the property

## Original description

Gets a Forge app property by property key. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestconfluence/#method-signature)** requests from Forge.
