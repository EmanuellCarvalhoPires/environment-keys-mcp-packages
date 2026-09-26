---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-settings
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/space/{spaceKey}/settings"
category: "Space settings"
writes_data: true
tool_note: "[[confluence_v1_update_space_settings]]"
---
# Confluence v1 - Update space settings

**Update space settings** — `PUT /wiki/rest/api/space/{spaceKey}/settings`

- Run by the tool [[confluence_v1_update_space_settings]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/settings
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space whose settings will be updated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the settings for a space.

**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
[`manage/space`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space.

**Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
