---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/themes
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/settings/theme/{themeKey}"
category: "Themes"
writes_data: false
tool_note: "[[confluence_v1_get_theme]]"
---
# Confluence v1 - Get theme

**Get theme** — `GET /wiki/rest/api/settings/theme/{themeKey}`

- Run by the tool [[confluence_v1_get_theme]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/settings/theme/{{param:themeKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `themeKey` (path, string, required) — The key of the theme to be returned.

## Original description

Returns a theme. This includes information about the theme name,
description, and icon.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: None
