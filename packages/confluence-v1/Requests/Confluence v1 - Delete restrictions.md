---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/content/{id}/restriction"
category: "Content restrictions"
writes_data: true
tool_note: "[[confluence_v1_delete_restrictions]]"
---
# Confluence v1 - Delete restrictions

**Delete restrictions** — `DELETE /wiki/rest/api/content/{id}/restriction`

- Run by the tool [[confluence_v1_delete_restrictions]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the content to remove restrictions from.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content restrictions (returned in response) to expand.

## Original description

Removes all restrictions (read and update) on a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the content.
