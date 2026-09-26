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
path: "/pages/{id}/classification-level"
category: "Classification Level"
writes_data: false
tool_note: "[[confluence_get_page_classification_level]]"
---
# Confluence v2 - Get page classification level

**Get page classification level** — `GET /pages/{id}/classification-level`

- Run by the tool [[confluence_get_page_classification_level]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/pages/{{param:id}}/classification-level?status={{param:status}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the page for which classification level should be returned.
- `status` (query, string, optional) — Status of page from which classification level will fetched.

## Original description

Returns the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
for a specific page.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Permission to access the Confluence site ('Can use' global permission) and permission to view the page.
'Permission to edit the page is required if trying to view classification level for a draft.
