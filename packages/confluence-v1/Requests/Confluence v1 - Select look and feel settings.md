---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/settings
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/settings/lookandfeel"
category: "Settings"
writes_data: true
tool_note: "[[confluence_v1_select_look_and_feel_settings]]"
---
# Confluence v1 - Select look and feel settings

**Select look and feel settings** — `PUT /wiki/rest/api/settings/lookandfeel`

- Run by the tool [[confluence_v1_select_look_and_feel_settings]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/settings/lookandfeel
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the look and feel settings to the default (global) settings, the
custom settings, or the current theme's settings for a space.
The custom and theme settings can only be selected if there is already
a theme set for a space. Note, the default space settings are inherited
from the current global settings.

**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
[`manage/look-and-feel`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space.

**Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
