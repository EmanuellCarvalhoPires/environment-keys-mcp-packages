---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-labels
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/content/{id}/label/{label}"
category: "Content labels"
writes_data: true
tool_note: "[[confluence_v1_remove_label_from_content]]"
---
# Confluence v1 - Remove label from content

**Remove label from content** — `DELETE /wiki/rest/api/content/{id}/label/{label}`

- Run by the tool [[confluence_v1_remove_label_from_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/content/{{param:id}}/label/{{param:label}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that the label will be removed from.
- `label` (path, string, required) — The name of the label to be removed.

## Original description

Removes a label from a piece of content. Labels can't be deleted from archived content.
This is similar to [Remove label from content using query parameter](#api-content-id-label-delete)
except that the label name is specified via a path parameter.

Use this method if the label name does not have "/" characters, as the path
parameter does not accept "/" characters for security reasons. Otherwise,
use [Remove label from content using query parameter](#api-content-id-label-delete).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to update the content.
