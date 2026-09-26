---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/settings
  - api/operation/action
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/settings/lookandfeel/custom"
category: "Settings"
writes_data: true
tool_note: "[[confluence_v1_update_look_and_feel_settings]]"
---
# Confluence v1 - Update look and feel settings

**Update look and feel settings** — `POST /wiki/rest/api/settings/lookandfeel/custom`

- Run by the tool [[confluence_v1_update_look_and_feel_settings]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/settings/lookandfeel/custom?spaceKey={{param:spaceKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `spaceKey` (query, string, optional) — The key of the space for which the look and feel settings will be updated. If this is not set, the global look and feel settings will be updated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the look and feel settings for the site or for a single space.
If custom settings exist, they are updated. If no custom settings exist,
then a set of custom settings is created.

Note, if a theme is selected for a space, the space look and feel settings
are provided by the theme and cannot be overridden.

**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:

- If `spaceKey` is specified, [`manage/look-and-feel`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space.
- If `spaceKey` is omitted, 'Confluence Administrator' global permission.

**Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
