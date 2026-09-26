---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/app-properties
  - api/operation/get
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/forge/1/app/properties/{propertyKey}"
category: "App properties"
writes_data: false
---
# Jira v3 - Get app property (Forge)

**Get app property (Forge)** — `GET /rest/forge/1/app/properties/{propertyKey}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get app property (Forge)"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/forge/1/app/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `propertyKey` (path, string, required) — The key of the property.

## Original description

Returns the value of a Forge app's property.

**[Permissions](#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.
