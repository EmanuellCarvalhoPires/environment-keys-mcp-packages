---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-states
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/space/{spaceKey}/state/settings"
category: "Content states"
writes_data: false
tool_note: "[[confluence_v1_get_content_state_settings_for_space]]"
---
# Confluence v1 - Get content state settings for space

**Get content state settings for space** — `GET /wiki/rest/api/space/{spaceKey}/state/settings`

- Run by the tool [[confluence_v1_get_content_state_settings_for_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/state/settings
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to be queried for its content state settings.

## Original description

Get object describing whether content states are allowed at all, if custom content states or space content states
are restricted, and a list of space content states allowed for the space if they are not restricted.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Admin' permission for the space.
