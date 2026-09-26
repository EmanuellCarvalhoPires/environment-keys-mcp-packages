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
path: "/wiki/rest/api/content/{id}/label"
category: "Content labels"
writes_data: true
tool_note: "[[confluence_v1_remove_label_from_content_using_query_parameter]]"
---
# Confluence v1 - Remove label from content using query parameter

**Remove label from content using query parameter** — `DELETE /wiki/rest/api/content/{id}/label`

- Run by the tool [[confluence_v1_remove_label_from_content_using_query_parameter]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/content/{{param:id}}/label?name={{param:name}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that the label will be removed from.
- `name` (query, string, required) — The name of the label to be removed.

## Original description

Removes a label from a piece of content. Labels can't be deleted from archived content.
This is similar to [Remove label from content](#api-content-id-label-label-delete)
except that the label name is specified via a query parameter.

Use this method if the label name has "/" characters, as
[Remove label from content using query parameter](#api-content-id-label-delete)
does not accept "/" characters for the label name.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to update the content.
