---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/app-properties
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/app/properties/{propertyKey}"
category: "App Properties"
writes_data: true
tool_note: "[[confluence_deletes_a_forge_app_property]]"
---
# Confluence v2 - Deletes a Forge app property

**Deletes a Forge app property.** — `DELETE /app/properties/{propertyKey}`

- Run by the tool [[confluence_deletes_a_forge_app_property]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/app/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `propertyKey` (path, string, required) — The key of the property

## Original description

Deletes a Forge app property. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestconfluence/#method-signature)** requests from Forge.
