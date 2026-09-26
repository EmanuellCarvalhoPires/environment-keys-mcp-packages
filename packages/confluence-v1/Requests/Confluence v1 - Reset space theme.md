---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/themes
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/space/{spaceKey}/theme"
category: "Themes"
writes_data: true
tool_note: "[[confluence_v1_reset_space_theme]]"
---
# Confluence v1 - Reset space theme

**Reset space theme** — `DELETE /wiki/rest/api/space/{spaceKey}/theme`

- Run by the tool [[confluence_v1_reset_space_theme]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/theme
Authorization: {{service.auth_token}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to reset the theme for.

## Original description

Resets the space theme. This means that the space will inherit the
global look and feel settings

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Admin' permission for the space.
