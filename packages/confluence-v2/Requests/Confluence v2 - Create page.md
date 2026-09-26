---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/page
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/pages"
category: "Page"
writes_data: true
tool_note: "[[confluence_create_page]]"
---
# Confluence v2 - Create page

**Create page** — `POST /pages`

- Run by the tool [[confluence_create_page]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/pages?embedded={{param:embedded}}&private={{param:private}}&root-level={{param:root_level}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `embedded` (query, string, optional) — Tag the content as embedded and content will be created in NCS.
- `private` (query, string, optional) — The page will be private. Only the user who creates this page will have permission to view and edit one.
- `root_level` (query, string, optional) — The page will be created at the root level of the space (outside the space homepage tree). If true, then a value may not be supplied for the parentId body parameter.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a page in the space.

Pages are created as published by default unless specified as a draft in the status field. If creating a published page, the title must be specified.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the corresponding space. Permission to create a page in the space.
