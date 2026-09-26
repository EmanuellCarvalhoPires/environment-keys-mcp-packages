---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/experimental
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/space/{spaceKey}/label"
category: "Experimental"
writes_data: true
tool_note: "[[confluence_v1_add_labels_to_a_space]]"
---
# Confluence v1 - Add labels to a space

**Add labels to a space** — `POST /wiki/rest/api/space/{spaceKey}/label`

- Run by the tool [[confluence_v1_add_labels_to_a_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/label
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to add labels to.
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
