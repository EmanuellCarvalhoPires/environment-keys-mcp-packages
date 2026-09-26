---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/settings
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/settings/lookandfeel"
category: "Settings"
writes_data: false
tool_note: "[[confluence_v1_get_look_and_feel_settings]]"
---
# Confluence v1 - Get look and feel settings

**Get look and feel settings** — `GET /wiki/rest/api/settings/lookandfeel`

- Run by the tool [[confluence_v1_get_look_and_feel_settings]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/settings/lookandfeel?spaceKey={{param:spaceKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `spaceKey` (query, string, optional) — The key of the space for which the look and feel settings will be returned. If this is not set, only the global look and feel settings are returned.

## Original description

Returns the look and feel settings for the site or a single space. This
includes attributes such as the color scheme, padding, and border radius.

The look and feel settings for a space can be inherited from the global
look and feel settings or provided by a theme.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
None
