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
path: "/footer-comments/{id}/versions/{version-number}"
category: "Version"
writes_data: false
tool_note: "[[confluence_get_version_details_for_footer_comment_version]]"
---
# Confluence v2 - Get version details for footer comment version

**Get version details for footer comment version** — `GET /footer-comments/{id}/versions/{version-number}`

- Run by the tool [[confluence_get_version_details_for_footer_comment_version]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/footer-comments/{{param:id}}/versions/{{param:version_number}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the footer comment for which version details should be returned.
- `version_number` (path, string, required) — The version number of the footer comment to be returned.

## Original description

Retrieves version details for the specified footer comment version.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page or blog post and its corresponding space.
