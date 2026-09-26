---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/themes
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/settings/theme"
category: "Themes"
writes_data: false
tool_note: "[[confluence_v1_get_themes]]"
---
# Confluence v1 - Get themes

**Get themes** — `GET /wiki/rest/api/settings/theme`

- Run by the tool [[confluence_v1_get_themes]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/settings/theme?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `start` (query, string, optional) — The starting index of the returned themes.
- `limit` (query, string, optional) — The maximum number of themes to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns all themes, not including the default theme.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: None
