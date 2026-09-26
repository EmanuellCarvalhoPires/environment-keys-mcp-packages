---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/app-properties
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/app/properties"
category: "App Properties"
writes_data: false
tool_note: "[[confluence_get_forge_app_properties]]"
---
# Confluence v2 - Get Forge app properties

**Get Forge app properties.** — `GET /app/properties`

- Run by the tool [[confluence_get_forge_app_properties]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/app/properties?cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `cursor` (query, string, optional) — Used for pagination, this opaque cursor represents the last returned property key. It will be included in the response body as the next link. Use this key to request the next set of results.
- `limit` (query, string, optional) — Maximum number of app properties per result to return. If more results exist, use the last returned property key from the Link field in the response body as a cursor to retrieve the next set of result…

## Original description

Gets Forge app properties. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestconfluence/#method-signature)** requests from Forge.
