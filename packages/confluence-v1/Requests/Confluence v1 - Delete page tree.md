---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/experimental
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/content/{id}/pageTree"
category: "Experimental"
writes_data: true
tool_note: "[[confluence_v1_delete_page_tree]]"
---
# Confluence v1 - Delete page tree

**Delete page tree** — `DELETE /wiki/rest/api/content/{id}/pageTree`

- Run by the tool [[confluence_v1_delete_page_tree]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/content/{{param:id}}/pageTree
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the content which forms root of the page tree, to be deleted.

## Original description

Moves a pagetree rooted at a page to the space's trash:

- If the content's type is `page` and its status is `current`, it will be trashed including
all its descendants.
- For every other combination of content type and status, this API is not supported.

This API accepts the pageTree delete request and returns a task ID.
The delete process happens asynchronously.

 Response example:
 
 {
      "id" : "1180606",
      "links" : {
           "status" : "/rest/api/longtask/1180606"
      }
 }
 
 Use the `/longtask/` REST API to get the copy task status.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Delete' permission for the space that the content is in.
