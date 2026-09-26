---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/themes
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/space/{spaceKey}/theme"
category: "Themes"
writes_data: true
tool_note: "[[confluence_v1_set_space_theme]]"
---
# Confluence v1 - Set space theme

**Set space theme** — `PUT /wiki/rest/api/space/{spaceKey}/theme`

- Run by the tool [[confluence_v1_set_space_theme]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/theme
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to set the theme for.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the theme for a space. Note, if you want to reset the space theme to
the default Confluence theme, use the 'Reset space theme' method instead
of this method.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Admin' permission for the space.
