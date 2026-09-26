---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/addon
  - api/operation/list
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/addon/{addon_key}/client-key"
category: "Addon"
writes_data: false
---
# Bitbucket - Get the client key of a Connect addon

**Get the client key of a Connect addon** — `GET /addon/{addon_key}/client-key`

- No dedicated tool.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/addon/{{param:addon_key}}/client-key
Authorization: {{service.auth_token}}
```

## Parameters

- `addon_key` (path, string, required) — Value of addonkey in the path.

## Original description

Get the client key of the Connect addon associated with a Forge app install via forgeAppId linkage.

This endpoint is part of the Connect -> Forge migration tooling. It is intended to be used by a Forge app
using `asApp().requestBitbucket()` only.
Prerequisite: app developer needs to register the linkage between their Connect and Forge app by setting
`forgeAppId` in the Connect addon descriptor to `app.id` from Forge app manifest, then update the installations.
If the request came from an installation of a registered Forge app, the client key of the linked Connect addon
installed in the same workspace will be returned.

```
api.asApp().requestBitbucket(route`/2.0/addon/{addon-key}/client-key`)
```
