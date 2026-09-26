---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/template
  - api/operation/update
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/template"
category: "Template"
writes_data: true
tool_note: "[[confluence_v1_update_content_template]]"
---
# Confluence v1 - Update content template

**Update content template** — `PUT /wiki/rest/api/template`

- Run by the tool [[confluence_v1_update_content_template]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/template
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates a content template. Note, blueprint templates cannot be updated
via the REST API.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Admin' permission for the space to update a space template or 'Confluence Administrator'
global permission to update a global template.
