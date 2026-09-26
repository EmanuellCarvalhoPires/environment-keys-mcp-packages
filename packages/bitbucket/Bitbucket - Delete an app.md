---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/addon
  - api/operation/delete
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/addon"
category: "Addon"
writes_data: true
---
# Bitbucket - Delete an app

**Delete an app** — `DELETE /addon`

- No dedicated tool.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/addon
Authorization: {{service.auth_token}}
```

## Original description

Deletes the application for the user.

This endpoint is intended to be used by Bitbucket Connect apps
and only supports JWT authentication -- that is how Bitbucket
identifies the particular installation of the app. Developers
with applications registered in the "Develop Apps" section
of Bitbucket Marketplace need not use this endpoint as
updates for those applications can be sent out via the
UI of that section.

```
$ curl -X DELETE https://api.bitbucket.org/2.0/addon \
  -H "Authorization: JWT "
```
