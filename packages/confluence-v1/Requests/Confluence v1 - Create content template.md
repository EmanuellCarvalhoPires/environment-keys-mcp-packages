---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/template
  - api/operation/create
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/template"
category: "Template"
writes_data: true
tool_note: "[[confluence_v1_create_content_template]]"
---
# Confluence v1 - Create content template

**Create content template** — `POST /wiki/rest/api/template`

- Run by the tool [[confluence_v1_create_content_template]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/template
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new content template. Note, blueprint templates cannot be created via the REST API.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Admin' permission for the space to create a space template or 'Confluence Administrator'
global permission to create a global template.
