---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/database
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/databases"
category: "Database"
writes_data: true
tool_note: "[[confluence_create_database]]"
---
# Confluence v2 - Create database

**Create database** — `POST /databases`

- Run by the tool [[confluence_create_database]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/databases?private={{param:private}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `private` (query, string, optional) — The database will be private. Only the user who creates this database will have permission to view and edit one.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a database in the space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the corresponding space. Permission to create a database in the space.
