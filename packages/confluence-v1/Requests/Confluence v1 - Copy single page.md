---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-children-and-descendants
  - api/operation/action
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/content/{id}/copy"
category: "Content - children and descendants"
writes_data: true
tool_note: "[[confluence_v1_copy_single_page]]"
---
# Confluence v1 - Copy single page

**Copy single page** — `POST /wiki/rest/api/content/{id}/copy`

- Run by the tool [[confluence_v1_copy_single_page]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/content/{{param:id}}/copy?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json;charset=UTF-8
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content to expand. Maximum sub-expansions allowed is 8.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Copies a single page and its associated properties, permissions, attachments, and custom contents.
 The `id` path parameter refers to the content ID of the page to copy. The target of the page to be copied
 is defined using the `destination` in the request body and can be one of the following types.

  - `space`: page will be copied to the specified space as a root page on the space
  - `parent_page`: page will be copied as a child of the specified parent page
  - `parent_content`: page will be copied as a child of the specified parent content
  - `existing_page`: page will be copied and replace the specified page

By default, the following objects are expanded: `space`, `history`, `version`.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Add' permission for the space that the content will be copied in and permission to update the content if copying to an `existing_page`.
