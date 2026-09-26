---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-labels
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/content/{id}/label"
category: "Content labels"
writes_data: true
tool_note: "[[confluence_v1_add_labels_to_content]]"
---
# Confluence v1 - Add labels to content

**Add labels to content** — `POST /wiki/rest/api/content/{id}/label`

- Run by the tool [[confluence_v1_add_labels_to_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/content/{{param:id}}/label
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that will have labels added to it.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds labels to a piece of content. Does not modify the existing labels.

Notes:

- Labels can also be added when creating content ([Create content](#api-content-post)).
- Labels can be updated when updating content ([Update content](#api-content-id-put)).
This will delete the existing labels and replace them with the labels in
the request.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to update the content.
