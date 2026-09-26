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
path: "/wiki/rest/api/space/{spaceKey}/theme"
category: "Themes"
writes_data: false
tool_note: "[[confluence_v1_get_space_theme]]"
---
# Confluence v1 - Get space theme

**Get space theme** — `GET /wiki/rest/api/space/{spaceKey}/theme`

- Run by the tool [[confluence_v1_get_space_theme]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/theme
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to be queried for its theme.

## Original description

Returns the theme selected for a space, if one is set. If no space
theme is set, this means that the space is inheriting the global look
and feel settings.

**[Permissions required](https://confluence.atlassian.com/x/_AozKw)**: ‘View’ permission for the space.
