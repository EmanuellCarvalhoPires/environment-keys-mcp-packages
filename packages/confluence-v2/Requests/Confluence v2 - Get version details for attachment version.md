---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/version
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/attachments/{attachment-id}/versions/{version-number}"
category: "Version"
writes_data: false
tool_note: "[[confluence_get_version_details_for_attachment_version]]"
---
# Confluence v2 - Get version details for attachment version

**Get version details for attachment version** — `GET /attachments/{attachment-id}/versions/{version-number}`

- Run by the tool [[confluence_get_version_details_for_attachment_version]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/attachments/{{param:attachment_id}}/versions/{{param:version_number}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `attachment_id` (path, string, required) — The ID of the attachment for which version details should be returned.
- `version_number` (path, string, required) — The version number of the attachment to be returned.

## Original description

Retrieves version details for the specified attachment and version number.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the attachment.
