---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-versions
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/content/{id}/version/{versionNumber}"
category: "Content versions"
writes_data: true
tool_note: "[[confluence_v1_delete_content_version]]"
---
# Confluence v1 - Delete content version

**Delete content version** — `DELETE /wiki/rest/api/content/{id}/version/{versionNumber}`

- Run by the tool [[confluence_v1_delete_content_version]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/content/{{param:id}}/version/{{param:versionNumber}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that the version will be deleted from.
- `versionNumber` (path, string, required) — The number of the version to be deleted. The version number starts from 1 up to current version.

## Original description

Delete a historical version. This does not delete the changes made to the
content in that version, rather the changes for the deleted version are
rolled up into the next version. Note, you cannot delete the current version.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to update the content.
