---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/action
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/whiteboards/{id}/classification-level/reset"
category: "Classification Level"
writes_data: true
tool_note: "[[confluence_reset_whiteboard_classification_level]]"
---
# Confluence v2 - Reset whiteboard classification level

**Reset whiteboard classification level** — `POST /whiteboards/{id}/classification-level/reset`

- Run by the tool [[confluence_reset_whiteboard_classification_level]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/whiteboards/{{param:id}}/classification-level/reset
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the whiteboard for which classification level should be updated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Resets the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
for a specific whiteboard for the space 
[default classification level](https://support.atlassian.com/security-and-access-policies/docs/what-is-a-default-classification-level/).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Permission to access the Confluence site ('Can use' global permission) and permission to view the whiteboard.
