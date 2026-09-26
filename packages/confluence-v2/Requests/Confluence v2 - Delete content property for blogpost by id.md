---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/blogposts/{blogpost-id}/properties/{property-id}"
category: "Content Properties"
writes_data: true
tool_note: "[[confluence_delete_content_property_for_blogpost_by_id]]"
---
# Confluence v2 - Delete content property for blogpost by id

**Delete content property for blogpost by id** — `DELETE /blogposts/{blogpost-id}/properties/{property-id}`

- Run by the tool [[confluence_delete_content_property_for_blogpost_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/blogposts/{{param:blogpost_id}}/properties/{{param:property_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `blogpost_id` (path, string, required) — The ID of the blog post the property belongs to.
- `property_id` (path, string, required) — The ID of the property to be deleted.

## Original description

Deletes a content property for a blogpost by its id. 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the blog post.
