---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-settings
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/space/{spaceKey}/settings"
category: "Space settings"
writes_data: false
tool_note: "[[confluence_v1_get_space_settings]]"
---
# Confluence v1 - Get space settings

**Get space settings** — `GET /wiki/rest/api/space/{spaceKey}/settings`

- Run by the tool [[confluence_v1_get_space_settings]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/settings
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to be queried for its settings.

## Original description

Returns the settings of a space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'View' permission for the space.
