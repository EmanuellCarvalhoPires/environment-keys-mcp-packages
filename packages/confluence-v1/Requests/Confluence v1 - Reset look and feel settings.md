---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/settings
  - api/operation/delete
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/settings/lookandfeel/custom"
category: "Settings"
writes_data: true
tool_note: "[[confluence_v1_reset_look_and_feel_settings]]"
---
# Confluence v1 - Reset look and feel settings

**Reset look and feel settings** — `DELETE /wiki/rest/api/settings/lookandfeel/custom`

- Run by the tool [[confluence_v1_reset_look_and_feel_settings]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/settings/lookandfeel/custom?spaceKey={{param:spaceKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `spaceKey` (query, string, optional) — The key of the space for which the look and feel settings will be reset. If this is not set, the global look and feel settings will be reset.

## Original description

Resets the custom look and feel settings for the site or a single space.
This changes the values of the custom settings to be the same as the
default settings. It does not change which settings (default or custom)
are selected. Note, the default space settings are inherited from the
current global settings.

**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:

- If `spaceKey` is specified, [`manage/look-and-feel`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space.
- If `spaceKey` is omitted, 'Confluence Administrator' global permission.

**Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
