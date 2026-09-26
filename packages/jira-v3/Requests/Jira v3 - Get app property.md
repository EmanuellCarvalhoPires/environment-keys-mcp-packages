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
path: "/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}"
category: "App properties"
writes_data: false
---
# Jira v3 - Get app property

**Get app property** — `GET /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get app property"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/atlassian-connect/1/addons/{{param:addonKey}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `addonKey` (path, string, required) — The key of the app, as defined in its descriptor.
- `propertyKey` (path, string, required) — The key of the property.

## Original description

Returns the key and value of an app's property. The property key `connect_client_key_019cdff3-8bfb-71fe-9628-875b700aebb8`
is reserved. It returns a synthetic, read-only property containing the Connect `clientKey` for the requested tenant.
This is intended for Forge apps with `app.connect.key` to retrieve the Connect client key during migration.

**[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).
