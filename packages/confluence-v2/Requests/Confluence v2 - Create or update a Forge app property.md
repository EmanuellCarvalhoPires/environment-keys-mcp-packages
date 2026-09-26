---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/app-properties
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/app/properties/{propertyKey}"
category: "App Properties"
writes_data: true
tool_note: "[[confluence_create_or_update_a_forge_app_property]]"
---
# Confluence v2 - Create or update a Forge app property

**Create or update a Forge app property.** — `PUT /app/properties/{propertyKey}`

- Run by the tool [[confluence_create_or_update_a_forge_app_property]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/app/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `propertyKey` (path, string, required) — The key of the property
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates or updates a Forge app property. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestconfluence/#method-signature)** requests from Forge.
