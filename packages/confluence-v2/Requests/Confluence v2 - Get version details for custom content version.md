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
path: "/custom-content/{custom-content-id}/versions/{version-number}"
category: "Version"
writes_data: false
tool_note: "[[confluence_get_version_details_for_custom_content_version]]"
---
# Confluence v2 - Get version details for custom content version

**Get version details for custom content version** — `GET /custom-content/{custom-content-id}/versions/{version-number}`

- Run by the tool [[confluence_get_version_details_for_custom_content_version]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/custom-content/{{param:custom_content_id}}/versions/{{param:version_number}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `custom_content_id` (path, string, required) — The ID of the custom content for which version details should be returned.
- `version_number` (path, string, required) — The version number of the custom content to be returned.

## Original description

Retrieves version details for the specified custom content and version number.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the page.
