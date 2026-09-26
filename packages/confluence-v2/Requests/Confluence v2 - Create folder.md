---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/folder
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/folders"
category: "Folder"
writes_data: true
tool_note: "[[confluence_create_folder]]"
---
# Confluence v2 - Create folder

**Create folder** — `POST /folders`

- Run by the tool [[confluence_create_folder]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/folders
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a folder in the space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the corresponding space. Permission to create a folder in the space.
