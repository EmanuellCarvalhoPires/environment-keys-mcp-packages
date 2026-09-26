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
path: "/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}"
category: "App properties"
writes_data: true
---
# Jira v3 - Delete app property

**Delete app property** — `DELETE /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Delete app property"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/atlassian-connect/1/addons/{{param:addonKey}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `addonKey` (path, string, required) — The key of the app, as defined in its descriptor.
- `propertyKey` (path, string, required) — The key of the property.

## Original description

Deletes an app's property.

**[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).
