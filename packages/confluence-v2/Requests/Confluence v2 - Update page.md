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
path: "/pages/{id}"
category: "Page"
writes_data: true
tool_note: "[[confluence_update_page]]"
---
# Confluence v2 - Update page

**Update page** — `PUT /pages/{id}`

- Run by the tool [[confluence_update_page]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/pages/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the page to be updated. If you don't know the page ID, use Get Pages and filter the results.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a page by id.

When the "current" version is updated, the provided body content is considered as the latest version. This latest body content
will be attempted to be merged into the draft version through a content reconciliation algorithm. If two versions are significantly diverged, 
the latest provided content may entirely override what was previously in the draft. 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the page and its corresponding space. Permission to update pages in the space.
