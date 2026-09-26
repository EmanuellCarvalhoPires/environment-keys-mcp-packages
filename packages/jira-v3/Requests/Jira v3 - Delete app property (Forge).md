---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/app-properties
  - api/operation/delete
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/forge/1/app/properties/{propertyKey}"
category: "App properties"
writes_data: true
---
# Jira v3 - Delete app property (Forge)

**Delete app property (Forge)** — `DELETE /rest/forge/1/app/properties/{propertyKey}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Delete app property (Forge)"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/forge/1/app/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `propertyKey` (path, string, required) — The key of the property.

## Original description

Deletes a Forge app's property.

**[Permissions](#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
