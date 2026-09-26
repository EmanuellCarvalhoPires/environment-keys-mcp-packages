---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/smart-link
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/embeds/{id}"
category: "Smart Link"
writes_data: true
tool_note: "[[confluence_delete_smart_link_in_the_content_tree]]"
---
# Confluence v2 - Delete Smart Link in the content tree

**Delete Smart Link in the content tree** — `DELETE /embeds/{id}`

- Run by the tool [[confluence_delete_smart_link_in_the_content_tree]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/embeds/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Smart Link in the content tree to be deleted.

## Original description

Delete a Smart Link in the content tree by id.

Deleting a Smart Link in the content tree moves the Smart Link to the trash, where it can be restored later

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the Smart Link in the content tree and its corresponding space.
Permission to delete Smart Links in the content tree in the space.
