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
path: "/wiki/rest/api/settings/theme/selected"
category: "Themes"
writes_data: false
tool_note: "[[confluence_v1_get_global_theme]]"
---
# Confluence v1 - Get global theme

**Get global theme** — `GET /wiki/rest/api/settings/theme/selected`

- Run by the tool [[confluence_v1_get_global_theme]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/settings/theme/selected
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the globally assigned theme.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: None
