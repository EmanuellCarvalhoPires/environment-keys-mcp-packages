---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/app-properties
  - api/operation/list
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/atlassian-connect/1/addons/{addonKey}/properties"
category: "App properties"
writes_data: false
---
# Jira v3 - Get app properties

**Get app properties** — `GET /rest/atlassian-connect/1/addons/{addonKey}/properties`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get app properties"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/atlassian-connect/1/addons/{{param:addonKey}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `addonKey` (path, string, required) — The key of the app, as defined in its descriptor.

## Original description

Gets all the properties of an app. The reserved key `connect_client_key_019cdff3-8bfb-71fe-9628-875b700aebb8` is not returned.

**[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).
