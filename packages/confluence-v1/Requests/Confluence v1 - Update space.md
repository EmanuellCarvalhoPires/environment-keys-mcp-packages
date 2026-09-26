---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/space/{spaceKey}"
category: "Space"
writes_data: true
tool_note: "[[confluence_v1_update_space]]"
---
# Confluence v1 - Update space

**Update space** — `PUT /wiki/rest/api/space/{spaceKey}`

- Run by the tool [[confluence_v1_update_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to update.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the name, description, or homepage of a space.

-   For security reasons, permissions cannot be updated via the API and
must be changed via the user interface instead.
-   Currently you cannot set space labels when updating a space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Admin' permission for the space.
