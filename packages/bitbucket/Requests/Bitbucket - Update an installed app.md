---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/addon
  - api/operation/update
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/addon"
category: "Addon"
writes_data: true
---
# Bitbucket - Update an installed app

**Update an installed app** — `PUT /addon`

- No dedicated tool.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/addon
Authorization: {{service.auth_token}}
```

## Original description

Updates the application installation for the user.

This endpoint is intended to be used by Bitbucket Connect apps
and only supports JWT authentication -- that is how Bitbucket
identifies the particular installation of the app. Developers
with applications registered in the "Develop Apps" section
of Bitbucket need not use this endpoint as updates for those
applications can be sent out via the UI of that section.

Passing an empty body will update the installation using the
existing descriptor URL.

```
$ curl -X PUT https://api.bitbucket.org/2.0/addon \
  -H "Authorization: JWT " \
  --header "Content-Type: application/json" \
  --data '{}'
```

The new `descriptor` for the installation can be also provided
in the body directly.

```
$ curl -X PUT https://api.bitbucket.org/2.0/addon \
  -H "Authorization: JWT " \
  --header "Content-Type: application/json" \
  --data '{"descriptor": $NEW_DESCRIPTOR}'
```

In both these modes the URL of the descriptor cannot be changed. To
change the descriptor location and upgrade an installation
the request must be made exclusively with a `descriptor_url`.

 ```
$ curl -X PUT https://api.bitbucket.org/2.0/addon \
  -H "Authorization: JWT " \
  --header "Content-Type: application/json" \
  --data '{"descriptor_url": $NEW_URL}'
```

The `descriptor_url` must exactly match the marketplace registration
that Atlassian has for the application. Contact your Atlassian
developer advocate to update this registration. Once the registration
has been updated you may call this resource for each installation.

Note that the scopes of the application cannot be increased
in the new descriptor nor reduced to none.
