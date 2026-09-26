---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-attachments
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/content/{id}/child/attachment/{attachmentId}/download"
category: "Content - attachments"
writes_data: false
tool_note: "[[confluence_v1_get_uri_to_download_attachment]]"
---
# Confluence v1 - Get URI to download attachment

**Get URI to download attachment** — `GET /wiki/rest/api/content/{id}/child/attachment/{attachmentId}/download`

- Run by the tool [[confluence_v1_get_uri_to_download_attachment]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/child/attachment/{{param:attachmentId}}/download?version={{param:version}}&status={{param:status}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that the attachment is attached to.
- `attachmentId` (path, string, required) — The ID of the attachment to download.
- `version` (query, string, optional) — The version of the attachment. If this parameter is absent, the redirect URI will download the latest version of the attachment.
- `status` (query, string, optional) — The statuses allowed on the retrieved attachment. If this parameter is absent, it will default to current.

## Original description

Redirects the client to a URL that serves an attachment's binary data.
