---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/pages/{id}/classification-level"
category: "Classification Level"
writes_data: true
tool_note: "[[confluence_update_page_classification_level]]"
---
# Confluence v2 - Update page classification level

**Update page classification level** — `PUT /pages/{id}/classification-level`

- Run by the tool [[confluence_update_page_classification_level]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/pages/{{param:id}}/classification-level
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the page for which classification level should be updated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
for a specific page.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Permission to access the Confluence site ('Can use' global permission) and permission to edit the page.
