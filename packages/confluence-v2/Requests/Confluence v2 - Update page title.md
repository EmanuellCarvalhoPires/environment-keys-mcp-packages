---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/page
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/pages/{id}/title"
category: "Page"
writes_data: true
tool_note: "[[confluence_update_page_title]]"
---
# Confluence v2 - Update page title

**Update page title** — `PUT /pages/{id}/title`

- Run by the tool [[confluence_update_page_title]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/pages/{{param:id}}/title
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the page to be updated. If you don't know the page ID, use Get Pages and filter the results
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the title of a specified page.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the page and its corresponding space. Permission to update pages in the space.
