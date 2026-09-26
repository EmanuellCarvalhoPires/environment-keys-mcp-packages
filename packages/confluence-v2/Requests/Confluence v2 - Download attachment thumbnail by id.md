---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/attachment
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/attachments/{id}/thumbnail/download"
category: "Attachment"
writes_data: false
tool_note: "[[confluence_download_attachment_thumbnail_by_id]]"
---
# Confluence v2 - Download attachment thumbnail by id

**Download attachment thumbnail by id** — `GET /attachments/{id}/thumbnail/download`

- Run by the tool [[confluence_download_attachment_thumbnail_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/attachments/{{param:id}}/thumbnail/download?version={{param:version}}&height={{param:height}}&width={{param:width}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the attachment to be returned. If you don't know the attachment's ID, use Get attachments for page/blogpost/custom content.
- `version` (query, string, optional) — Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
- `height` (query, string, optional) — Allows you to define the thumbnail height.
- `width` (query, string, optional) — Allows you to define the thumbnail width.

## Original description

Redirects the client to a URL that serves an attachment thumbnail's binary data.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the attachment's container.
