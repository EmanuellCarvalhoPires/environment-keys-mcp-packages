---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/app-properties
  - api/operation/update
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}"
category: "App properties"
writes_data: true
---
# Jira v3 - Set app property

**Set app property** — `PUT /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Set app property"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/atlassian-connect/1/addons/{{param:addonKey}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `addonKey` (path, string, required) — The key of the app, as defined in its descriptor.
- `propertyKey` (path, string, required) — The key of the property.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the value of an app's property. Use this resource to store custom data for your app.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).
