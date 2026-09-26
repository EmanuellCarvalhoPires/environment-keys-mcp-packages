---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-children-and-descendants
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/content/{pageId}/move/{position}/{targetId}"
category: "Content - children and descendants"
writes_data: true
tool_note: "[[confluence_v1_move_a_page_to_a_new_location_relative_to_a_target]]"
---
# Confluence v1 - Move a page to a new location relative to a target page

**Move a page to a new location relative to a target page** — `PUT /wiki/rest/api/content/{pageId}/move/{position}/{targetId}`

- Run by the tool [[confluence_v1_move_a_page_to_a_new_location_relative_to_a_target]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/content/{{param:pageId}}/move/{{param:position}}/{{param:targetId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (path, string, required) — The ID of the page to be moved
- `position` (path, string, required) — The position to move the page to relative to the target page: before - move the page under the same parent as the target, before the target in the list of children after - move the page under the same…
- `targetId` (path, string, required) — The ID of the target page for this operation

## Original description

Move a page to a new location relative to a target page:

* `before` - move the page under the same parent as the target, before the target in the list of children
* `after` - move the page under the same parent as the target, after the target in the list of children
* `append` - move the page to be a child of the target

Caution: This API can move pages to the top level of a space. Top-level pages are difficult to find in the UI
because they do not show up in the page tree display. To avoid this, never use `before` or `after` positions
when the `targetId` is a top-level page.
