---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/whiteboards/{id}/classification-level"
category: "Classification Level"
writes_data: false
tool_note: "[[confluence_get_whiteboard_classification_level]]"
---
# Confluence v2 - Get whiteboard classification level

**Get whiteboard classification level** — `GET /whiteboards/{id}/classification-level`

- Run by the tool [[confluence_get_whiteboard_classification_level]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/whiteboards/{{param:id}}/classification-level
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the whiteboard for which classification level should be returned.

## Original description

Returns the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
for a specific whiteboard.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Permission to access the Confluence site ('Can use' global permission) and permission to view the whiteboard.
