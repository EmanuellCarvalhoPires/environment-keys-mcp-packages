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
path: "/rest/forge/1/app/properties/{propertyKey}"
category: "App properties"
writes_data: true
---
# Jira v3 - Set app property (Forge)

**Set app property (Forge)** — `PUT /rest/forge/1/app/properties/{propertyKey}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Set app property (Forge)"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/forge/1/app/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `propertyKey` (path, string, required) — The key of the property.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the value of a Forge app's property.
These values can be retrieved in [Jira expressions](/cloud/jira/platform/jira-expressions/)
through the `app` [context variable](/cloud/jira/platform/jira-expressions/#context-variables).
They are also available in [entity property display conditions](/platform/forge/manifest-reference/display-conditions/entity-property-conditions/).

For other use cases, use the [Storage API](/platform/forge/runtime-reference/storage-api/).

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
